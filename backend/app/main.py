import random
import string

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .auth import create_token, get_current_user, hash_password, verify_password
from .database import Base, engine, get_db
from .models import Click, Url, User

Base.metadata.create_all(bind=engine)

app = FastAPI()


class RegisterRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.post("/auth/register")
def register(body: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == body.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=body.email, password_hash=hash_password(body.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "Account created", "user_id": user.id}


@app.post("/auth/login")
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_token(user.id)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/shorten")
def shorten_url(url: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    new_url = Url(original_url=url, short_code=code, user_id=current_user.id)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return {"short_code": code, "original_url": url, "owner": current_user.email}


@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(Url).filter(Url.short_code == short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    click = Click(url_id=url.id)
    db.add(click)
    db.commit()
    return RedirectResponse(url=url.original_url)

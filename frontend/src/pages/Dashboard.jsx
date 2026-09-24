import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { API_URL } from '../api'

export default function Dashboard() {
  const [urls, setUrls] = useState([])
  const [newUrl, setNewUrl] = useState('')
  const [error, setError] = useState('')
  const navigate = useNavigate()
  const token = localStorage.getItem('token')

  useEffect(() => {
    if (!token) {
      navigate('/login')
      return
    }
    fetchUrls()
  }, [])

  async function fetchUrls() {
    const res = await fetch(`${API_URL}/urls`, {
      headers: { Authorization: `Bearer ${token}` },
    })
    if (res.ok) {
      setUrls(await res.json())
    } else if (res.status === 401) {
      navigate('/login')
    }
  }

  async function handleShorten(e) {
    e.preventDefault()
    setError('')
    const res = await fetch(`${API_URL}/shorten?url=${encodeURIComponent(newUrl.trim())}`, {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
    })
    if (res.ok) {
      setNewUrl('')
      fetchUrls()
    } else {
      const err = await res.json()
      setError(err.detail)
    }
  }

  function logout() {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>My URLs</h1>
        <button onClick={logout} className="logout-btn">Logout</button>
      </div>

      <form onSubmit={handleShorten} className="shorten-form">
        <input
          type="url"
          placeholder="https://example.com"
          value={newUrl}
          onChange={e => setNewUrl(e.target.value)}
          required
        />
        <button type="submit">Shorten</button>
      </form>
      {error && <p className="error">{error}</p>}

      <table>
        <thead>
          <tr>
            <th>Original URL</th>
            <th>Short Code</th>
            <th>Clicks</th>
          </tr>
        </thead>
        <tbody>
          {urls.length === 0 ? (
            <tr>
              <td colSpan="3" style={{ textAlign: 'center', color: '#888' }}>
                No URLs yet. Shorten your first one above!
              </td>
            </tr>
          ) : (
            urls.map(url => (
              <tr key={url.id}>
                <td>
                  <a href={url.original_url} target="_blank" rel="noreferrer">
                    {url.original_url}
                  </a>
                </td>
                <td>
                  <a href={`${API_URL}/${url.short_code}`} target="_blank" rel="noreferrer">
                    {url.short_code}
                  </a>
                </td>
                <td>{url.clicks}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}

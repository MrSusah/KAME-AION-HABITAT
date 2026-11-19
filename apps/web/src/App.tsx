
import { useEffect, useState } from 'react'
import './App.css'

type DashboardSummary = {
  agents: { total: number; active: number }
  tasks: { running: number }
  approvals: { pending: number }
  runtime: string
  integrations: {
    database: string
    ai_gateway: string
    tool_gateway: string
  }
}

const API_BASE = '/api/v1'

const navigation = [
  { label: 'Overview', icon: '◫', section: 'WORKSPACE' },
  { label: 'Agents', icon: '◉', section: 'WORKSPACE' },
  { label: 'Projects & Tasks', icon: '▤', section: 'WORKSPACE' },
  { label: 'Virtual Office', icon: '⌂', section: 'WORKSPACE' },
  { label: 'AI Gateway', icon: '✳', section: 'SYSTEM' },
  { label: 'Tool Gateway', icon: '⌘', section: 'SYSTEM' },
  { label: 'Skills Library', icon: '▧', section: 'SYSTEM' },
  { label: 'Memory & Knowledge', icon: '◈', section: 'SYSTEM' },
  { label: 'Approvals', icon: '✓', section: 'CONTROL' },
  { label: 'Audit Logs', icon: '≡', section: 'CONTROL' },
  { label: 'Settings', icon: '⚙', section: 'CONTROL' },
]

function statusLabel(value: string) {
  return value.replaceAll('_', ' ')
}

function App() {
  const [summary, setSummary] = useState<DashboardSummary | null>(null)
  const [apiState, setApiState] = useState<'loading' | 'connected' | 'error'>('loading')
  const [activePage, setActivePage] = useState('Overview')
  const [lastUpdated, setLastUpdated] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false

    async function loadDashboard() {
      try {
        const response = await fetch(`${API_BASE}/dashboard/summary`)

        if (!response.ok) {
          throw new Error(`API returned ${response.status}`)
        }

        const data: DashboardSummary = await response.json()

        if (!cancelled) {
          setSummary(data)
          setApiState('connected')
          setLastUpdated(new Date().toLocaleTimeString())
        }
      } catch {
        if (!cancelled) {
          setApiState('error')
        }
      }
    }

    loadDashboard()
    const interval = window.setInterval(loadDashboard, 15000)

    return () => {
      cancelled = true
      window.clearInterval(interval)
    }
  }, [])

  const isOverview = activePage === 'Overview'

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">K</div>
          <div className="brand-copy">
            <strong>KAME <span>AION</span></strong>
            <small>THE LIVING AI OFFICE</small>
          </div>
        </div>

        <div className="workspace-switcher">
          <div className="workspace-avatar">A</div>
          <div className="workspace-copy">
            <strong>AION Habitat</strong>
            <small>Personal workspace</small>
          </div>
          <span className="switcher-arrow">⌄</span>
        </div>

        <nav className="navigation" aria-label="Main navigation">
          {['WORKSPACE', 'SYSTEM', 'CONTROL'].map((section) => (
            <div className="nav-section" key={section}>
              <p className="nav-heading">{section}</p>
              {navigation
                .filter((item) => item.section === section)
                .map((item) => (
                  <button
                    key={item.label}
                    className={`nav-item ${activePage === item.label ? 'active' : ''}`}
                    onClick={() => setActivePage(item.label)}
                    type="button"
                  >
                    <span className="nav-icon">{item.icon}</span>
                    <span>{item.label}</span>
                    {item.label === 'Approvals' && summary?.approvals.pending ? (
                      <span className="nav-count">{summary.approvals.pending}</span>
                    ) : null}
                  </button>
                ))}
            </div>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <div className="sidebar-status">
            <span className={`status-dot ${apiState}`} />
            <div>
              <strong>{apiState === 'connected' ? 'API Connected' : apiState === 'loading' ? 'Connecting API' : 'API Unavailable'}</strong>
              <small>Local development</small>
            </div>
          </div>
          <div className="user-profile">
            <div className="user-avatar">K</div>
            <div>
              <strong>Workspace Owner</strong>
              <small>Administrator</small>
            </div>
            <span className="profile-menu">•••</span>
          </div>
        </div>
      </aside>

      <main className="main-area">
        <header className="topbar">
          <div className="breadcrumb">
            <span>Workspace</span>
            <span className="breadcrumb-separator">/</span>
            <strong>{activePage}</strong>
          </div>
          <div className="topbar-actions">
            <div className="environment-tag">
              <span className="status-dot" />
              LOCAL ENVIRONMENT
            </div>
            <button className="icon-button" type="button" aria-label="Notifications">♧</button>
            <div className="topbar-avatar">K</div>
          </div>
        </header>

        <div className="page-content">
          {isOverview ? (
            <>
              <section className="welcome-row">
                <div>
                  <p className="eyebrow">WORKSPACE OVERVIEW</p>
                  <h1>Good day. <span>Welcome to AION.</span></h1>
                  <p className="page-subtitle">Your command center for a coordinated AI workforce.</p>
                </div>
                <div className="date-display">
                  <span className="date-icon">◷</span>
                  <div>
                    <strong>{new Date().toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric' })}</strong>
                    <small>{lastUpdated ? `Updated at ${lastUpdated}` : 'Waiting for first update'}</small>
                  </div>
                </div>
              </section>

              <section className="metrics-grid" aria-label="Workspace metrics">
                <article className="metric-card">
                  <div className="metric-top">
                    <span className="metric-icon violet">◉</span>
                    <span className="metric-caption">WORKFORCE</span>
                  </div>
                  <p className="metric-value">{summary ? summary.agents.total : '—'}</p>
                  <p className="metric-label">Total agents</p>
                  <div className="metric-foot">{summary ? `${summary.agents.active} active` : 'Loading agent data'}</div>
                </article>

                <article className="metric-card">
                  <div className="metric-top">
                    <span className="metric-icon blue">▤</span>
                    <span className="metric-caption">EXECUTION</span>
                  </div>
                  <p className="metric-value">{summary ? summary.tasks.running : '—'}</p>
                  <p className="metric-label">Running tasks</p>
                  <div className="metric-foot">Live execution records</div>
                </article>

                <article className="metric-card">
                  <div className="metric-top">
                    <span className="metric-icon amber">✓</span>
                    <span className="metric-caption">SUPERVISION</span>
                  </div>
                  <p className="metric-value">{summary ? summary.approvals.pending : '—'}</p>
                  <p className="metric-label">Pending approvals</p>
                  <div className="metric-foot">Awaiting owner review</div>
                </article>

                <article className="metric-card">
                  <div className="metric-top">
                    <span className="metric-icon green">⌁</span>
                    <span className="metric-caption">RUNTIME</span>
                  </div>
                  <p className="metric-value metric-state">{summary ? statusLabel(summary.runtime) : '—'}</p>
                  <p className="metric-label">Runtime status</p>
                  <div className="metric-foot">Backend-reported state</div>
                </article>
              </section>

              <section className="content-grid">
                <article className="panel office-panel">
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">SPATIAL WORKSPACE</p>
                      <h2>Virtual Office</h2>
                    </div>
                    <span className="panel-tag">PREVIEW</span>
                  </div>

                  <div className="office-scene">
                    <div className="scene-glow" />
                    <div className="office-floor">
                      <div className="office-room room-one">
                        <span className="room-label">COMMAND CENTER</span>
                        <div className="desk"><span className="desk-screen">A</span></div>
                        <div className="chair" />
                      </div>
                      <div className="office-room room-two">
                        <span className="room-label">AGENT WORKSPACE</span>
                        <div className="desk"><span className="desk-screen">AI</span></div>
                        <div className="chair" />
                      </div>
                      <div className="office-room room-three">
                        <span className="room-label">KNOWLEDGE HUB</span>
                        <div className="shelf"><i /><i /><i /></div>
                      </div>
                      <div className="scene-center-mark">K</div>
                    </div>
                  </div>
                  <div className="office-footer">
                    <span><span className="status-dot muted" /> Visual environment preview</span>
                    <span>Runtime state is authoritative</span>
                  </div>
                </article>

                <article className="panel system-panel">
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">INFRASTRUCTURE</p>
                      <h2>System Status</h2>
                    </div>
                    <span className={`connection-pill ${apiState}`}>
                      <span className="status-dot" />
                      {apiState === 'connected' ? 'Connected' : apiState === 'loading' ? 'Checking' : 'Offline'}
                    </span>
                  </div>

                  <div className="system-list">
                    <div className="system-row">
                      <div className="system-symbol">DB</div>
                      <div className="system-info"><strong>PostgreSQL</strong><small>Primary database</small></div>
                      <span className="system-state">{summary ? statusLabel(summary.integrations.database) : 'checking'}</span>
                    </div>
                    <div className="system-row">
                      <div className="system-symbol ai-symbol">AI</div>
                      <div className="system-info"><strong>AI Gateway</strong><small>Model connectivity</small></div>
                      <span className="system-state">{summary ? statusLabel(summary.integrations.ai_gateway) : 'checking'}</span>
                    </div>
                    <div className="system-row">
                      <div className="system-symbol tool-symbol">TG</div>
                      <div className="system-info"><strong>Tool Gateway</strong><small>Controlled tool access</small></div>
                      <span className="system-state">{summary ? statusLabel(summary.integrations.tool_gateway) : 'checking'}</span>
                    </div>
                  </div>

                  {apiState === 'error' && (
                    <div className="api-error" role="status">
                      Cannot reach the dashboard API. Check that the FastAPI server is running.
                    </div>
                  )}

                  <div className="system-note">
                    <span className="info-icon">i</span>
                    Services marked not configured have not yet been connected.
                  </div>
                </article>
              </section>

              <section className="bottom-grid">
                <article className="panel activity-panel">
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">OPERATIONS</p>
                      <h2>Recent Activity</h2>
                    </div>
                    <span className="panel-tag">LIVE DATA</span>
                  </div>
                  <div className="empty-state">
                    <div className="empty-icon">⌁</div>
                    <strong>No activity recorded</strong>
                    <p>Execution events will appear here when the Runtime is implemented and connected.</p>
                  </div>
                </article>

                <article className="panel control-panel">
                  <div className="panel-header">
                    <div>
                      <p className="eyebrow">GOVERNANCE</p>
                      <h2>Control & Safety</h2>
                    </div>
                  </div>
                  <div className="safety-item">
                    <span className="safety-icon">✓</span>
                    <div><strong>Supervised autonomy</strong><small>Approval workflow not yet connected</small></div>
                    <span className="state-label">Planned</span>
                  </div>
                  <div className="safety-item">
                    <span className="safety-icon">Ⅱ</span>
                    <div><strong>Emergency Stop</strong><small>Runtime control not yet implemented</small></div>
                    <span className="state-label">Planned</span>
                  </div>
                </article>
              </section>
            </>
          ) : (
            <section className="coming-soon panel">
              <p className="eyebrow">AION HABITAT MODULE</p>
              <div className="coming-icon">✳</div>
              <h1>{activePage}</h1>
              <p>This workspace module is part of the product roadmap and has not been implemented yet.</p>
              <button className="back-button" onClick={() => setActivePage('Overview')} type="button">
                Return to Overview
              </button>
            </section>
          )}

          <footer className="page-footer">
            <span>KAME AION HABITAT <span className="footer-separator">·</span> The Living AI Office</span>
            <span>Foundation build <span className="footer-separator">·</span> v0.1.0</span>
          </footer>
        </div>
      </main>
    </div>
  )
}

export default App

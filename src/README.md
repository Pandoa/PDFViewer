<div class="pv-hero">
  <div class="pv-hero-content">
    <div class="pv-tag">
      <span class="pv-tag-dot"></span>{{tag}}
    </div>
    <h1>{{hero_title}}</h1>
    <p class="pv-subtitle">{{hero_subtitle}}</p>
    <div class="pv-actions">
      <a class="pv-button" href="https://www.fab.com/listings/4b675d25-f2f9-4537-b2f3-5406b846f6ac">
        <span>{{primary_cta_text}}</span>
        <img alt="{{cta_icon_alt}}" class="pv-button-icon" src="https://pandoa.github.io/FirebaseFeatures/_images/buyueicon.png">
      </a>
      <a class="pv-button-secondary" href="#/umg">Quickstart documentation</a>
    </div>
  </div>
  <div class="pv-preview-wrap">
    <div class="pv-preview-glow"></div>
    <img alt="{{hero_image_alt}}" class="pv-preview" src="_images/Result3D.png">
  </div>
</div><div class="pv-section">
  <div class="pv-section-header">
    <span>{{section_getting_started}}</span>
    <h2>{{docs_title}}</h2>
  </div>
  <div class="pv-grid">
    <a class="pv-card-step" href="#/umg">
      <div class="pv-card-top">
        <div class="pv-card-icon">UI</div>
        <span class="pv-badge">UMG Widget</span>
      </div>
      <div class="pv-card-body">
        <h3>Render PDF in UMG</h3>
        <p>Display document pages dynamically inside Blueprint UI layouts.</p>
        <div class="pv-step-preview">
          <div class="pv-step-item">
            <span class="pv-step-num">1</span>
            <div class="pv-step-content">
              <strong>Create Widget Blueprint</strong>
              <span>Add a <code>UImage</code> component and mark it as <code>Is Variable</code>.</span>
            </div>
          </div>
          <div class="pv-step-item">
            <span class="pv-step-num">2</span>
            <div class="pv-step-content">
              <strong>Render PDF Page</strong>
              <span>Load document, render first page to a texture target.</span>
            </div>
          </div>
          <div class="pv-step-item">
            <span class="pv-step-num">3</span>
            <div class="pv-step-content">
              <strong>Assign & Display</strong>
              <span>Pass texture to image brush and configure resolution.</span>
            </div>
          </div>
        </div>
      </div>
      <div class="pv-card-footer-link">
        <span>Read Full UMG Guide</span>
        <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><line x1="5" x2="19" y1="12" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </div>
    </a>    <a class="pv-card-step" href="#/world">
      <div class="pv-card-top">
        <div class="pv-card-icon">3D</div>
        <span class="pv-badge">World Actor</span>
      </div>
      <div class="pv-card-body">
        <h3>Render PDF in World</h3>
        <p>Project documents onto 3D surfaces and meshes in the viewport.</p>
        <div class="pv-step-preview">
          <div class="pv-step-item">
            <span class="pv-step-num">1</span>
            <div class="pv-step-content">
              <strong>Create Actor Blueprint</strong>
              <span>Add a <code>Plane</code> or custom mesh component.</span>
            </div>
          </div>
          <div class="pv-step-item">
            <span class="pv-step-num">2</span>
            <div class="pv-step-content">
              <strong>Create Material</strong>
              <span>Set Shading Model to <code>Unlit</code> for clear readability.</span>
            </div>
          </div>
          <div class="pv-step-item">
            <span class="pv-step-num">3</span>
            <div class="pv-step-content">
              <strong>Apply Texture Param</strong>
              <span>Bind dynamic material instance to PDF stream.</span>
            </div>
          </div>
        </div>
      </div>
      <div class="pv-card-footer-link">
        <span>Read Full World Guide</span>
        <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><line x1="5" x2="19" y1="12" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </div>
    </a>
  </div>
</div><div class="pv-section">
  <div class="pv-section-header">
    <span>{{section_api}}</span>
    <h2>{{api_title}}</h2>
  </div>
  <div class="pv-grid">
    <a class="pv-card" href="#/document">
      <div class="pv-card-top">
        <div class="pv-card-icon">DOC</div>
        <div class="pv-arrow">
          <svg fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20"><line x1="5" x2="19" y1="12" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
      </div>
      <div class="pv-card-body">
        <h3>{{api_document_title}}</h3>
        <p>{{api_document_description}}</p>
      </div>
    </a>    <a class="pv-card" href="#/page">
      <div class="pv-card-top">
        <div class="pv-card-icon">PG</div>
        <div class="pv-arrow">
          <svg fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="20"><line x1="5" x2="19" y1="12" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
      </div>
      <div class="pv-card-body">
        <h3>{{api_page_title}}</h3>
        <p>{{api_page_description}}</p>
      </div>
    </a>
  </div>
</div><a class="pv-support" href="#/troubleshoting">
  <div class="pv-support-content">
    <span>{{support_label}}</span>
    <h3>{{support_title}}</h3>
    <p>{{support_description}}</p>
  </div>
  <div class="pv-support-arrow">
    <span>{{support_cta}}</span>
    <svg fill="none" height="18" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="18"><line x1="5" x2="19" y1="12" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </div>
</a><style>
  :root {
    --pv-accent: #fd8ce5;
    --pv-accent-glow: rgba(253, 140, 229, 0.12);
    --pv-accent-hover: #ffadfa;
    --pv-bg-card: #121216;
    --pv-border: rgba(255, 255, 255, 0.08);
    --pv-border-hover: rgba(253, 140, 229, 0.4);
    --pv-text-muted: #9aa0a6;
    --pv-text-heading: #f1f3f4;
  }  /* Reset & Layout Scaffolding */
  .pv-hero, .pv-section, .pv-support {
    box-sizing: border-box;
  }  .pv-hero {
    display: grid;
    grid-template-columns: 1fr 380px;
    gap: 48px;
    align-items: center;
    padding: 32px 0 48px;
  }  .pv-hero-content {
    min-width: 0;
  }  .pv-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    height: 26px;
    padding: 0 10px;
    border-radius: 6px;
    background: rgba(253, 140, 229, 0.1);
    border: 1px solid rgba(253, 140, 229, 0.2);
    color: var(--pv-accent);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }  .pv-tag-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--pv-accent);
  }  .pv-hero h1 {
    margin: 16px 0 0;
    font-size: clamp(32px, 4vw, 48px);
    line-height: 1.15;
    letter-spacing: -0.02em;
    font-weight: 700;
    color: var(--pv-text-heading);
  }  .pv-subtitle {
    margin: 16px 0 0;
    max-width: 580px;
    font-size: 16px;
    line-height: 1.6;
    color: var(--pv-text-muted);
  }  .pv-actions {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-top: 28px;
  }  .pv-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    height: 42px;
    padding: 0 20px;
    border-radius: 8px;
    background: var(--pv-accent);
    color: #0d0d11 !important;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    text-decoration: none !important;
    transition: background 0.2s ease, transform 0.2s ease;
  }  .pv-button:hover {
    background: var(--pv-accent-hover);
    transform: translateY(-1px);
  }  .pv-button-secondary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 42px;
    padding: 0 18px;
    border-radius: 8px;
    background: transparent;
    border: 1px solid var(--pv-border);
    color: var(--pv-text-heading);
    font-size: 13px;
    font-weight: 600;
    text-decoration: none !important;
    transition: background 0.2s ease, border-color 0.2s ease;
  }  .pv-button-secondary:hover {
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.2);
  }  .pv-button-icon {
    width: 16px;
    height: 16px;
    flex: none;
    filter: brightness(0.1) !important;
  }  .pv-preview-wrap {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
  }  .pv-preview-glow {
    position: absolute;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at center, var(--pv-accent-glow) 0%, transparent 70%);
    filter: blur(30px);
    z-index: 0;
    pointer-events: none;
  }  .pv-preview {
    position: relative;
    z-index: 1;
    display: block;
    height: auto;
    max-height: 260px;
    object-fit: contain;
    border-radius: 12px;
    border: 1px solid var(--pv-border);
    background: #09090b;
  }  .pv-section {
    margin-top: 56px;
  }  .pv-section-header {
    margin-bottom: 20px;
  }  .pv-section-header span {
    display: block;
    margin-bottom: 6px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--pv-accent);
    text-transform: uppercase;
  }  .pv-section-header h2 {
    margin: 0;
    font-size: 22px;
    line-height: 1.3;
    font-weight: 700;
    color: var(--pv-text-heading);
  }  .pv-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
  }  /* Cards Setup */
  .pv-card-step, .pv-card {
    display: flex;
    flex-direction: column;
    padding: 20px;
    border-radius: 12px;
    background: var(--pv-bg-card);
    border: 1px solid var(--pv-border);
    text-decoration: none !important;
    transition: border-color 0.2s ease, transform 0.2s ease;
  }  .pv-card-step {
    justify-content: space-between;
  }  .pv-card-step:hover, .pv-card:hover {
    border-color: var(--pv-border-hover);
    transform: translateY(-2px);
  }  .pv-card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
  }  .pv-card-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 24px;
    padding: 0 8px;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--pv-border);
    font-size: 11px;
    font-weight: 700;
    color: var(--pv-text-muted);
  }  .pv-badge {
    font-size: 11px;
    font-weight: 600;
    color: var(--pv-accent);
    background: rgba(253, 140, 229, 0.08);
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid rgba(253, 140, 229, 0.15);
  }  .pv-card-body h3, .pv-card-step h3 {
    margin: 0;
    font-size: 16px;
    line-height: 1.4;
    font-weight: 600;
    color: var(--pv-text-heading);
  }  .pv-card-body p, .pv-card-step p {
    margin: 6px 0 0;
    font-size: 13px;
    line-height: 1.5;
    color: var(--pv-text-muted);
  }  /* Step Preview Inner Details */
  .pv-step-preview {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 16px;
    padding: 12px 14px;
    border-radius: 8px;
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.04);
  }  .pv-step-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }  .pv-step-num {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 18px;
    height: 18px;
    flex-shrink: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.08);
    font-size: 10px;
    font-weight: 700;
    color: var(--pv-text-heading);
    margin-top: 2px;
  }  .pv-step-content {
    display: flex;
    flex-direction: column;
    gap: 2px;
    font-size: 12px;
    line-height: 1.4;
    color: var(--pv-text-muted);
  }  .pv-step-content strong {
    color: var(--pv-text-heading);
    font-weight: 600;
  }  .pv-step-content code {
    font-family: monospace;
    background: rgba(255, 255, 255, 0.08);
    padding: 1px 4px;
    border-radius: 3px;
    color: var(--pv-accent);
    font-size: 11px;
  }  .pv-card-footer-link {
    display: inline-flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 20px;
    padding-top: 12px;
    border-top: 1px solid var(--pv-border);
    color: var(--pv-accent);
    font-size: 13px;
    font-weight: 600;
  }  .pv-arrow {
    display: flex;
    align-items: center;
    color: var(--pv-text-muted);
    transition: color 0.2s ease, transform 0.2s ease;
  }  .pv-card:hover .pv-arrow {
    color: var(--pv-accent);
    transform: translateX(3px);
  }  /* Support Banner */
  .pv-support {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    margin-top: 40px;
    padding: 20px 24px;
    border-radius: 12px;
    text-decoration: none !important;
    background: var(--pv-bg-card);
    border: 1px solid var(--pv-border);
    transition: border-color 0.2s ease;
  }  .pv-support:hover {
    border-color: var(--pv-border-hover);
  }  .pv-support-content span {
    display: block;
    margin-bottom: 4px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--pv-text-muted);
    text-transform: uppercase;
  }  .pv-support h3 {
    margin: 0;
    font-size: 16px;
    font-weight: 600;
    color: var(--pv-text-heading);
  }  .pv-support p {
    margin: 4px 0 0;
    font-size: 13px;
    color: var(--pv-text-muted);
  }  .pv-support-arrow {
    display: flex;
    align-items: center;
    gap: 8px;
    flex: none;
    font-size: 13px;
    font-weight: 600;
    color: var(--pv-accent);
  }  /* Responsive Adjustments */
  @media (max-width: 900px) {
    .pv-hero {
      grid-template-columns: 1fr;
      gap: 32px;
      padding: 24px 0 32px;
    }
    .pv-preview-wrap {
      max-width: 100%;
    }
  }  @media (max-width: 640px) {
    .pv-grid {
      grid-template-columns: 1fr;
    }
    .pv-support {
      flex-direction: column;
      align-items: flex-start;
      gap: 16px;
    }
    .pv-support-arrow {
      width: 100%;
      justify-content: space-between;
    }
  }
</style>
.site-navbar-wrap {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1100;
    padding-top: 1rem;
    pointer-events: none;
}

.site-navbar-wrap > .container-lg,
.site-navbar-wrap > .container-fluid,
.site-navbar-wrap .container-lg,
.site-navbar-wrap .container-fluid {
    pointer-events: none;
}

.navbar-shell-premium,
.navbar-shell-premium * {
    pointer-events: auto;
}

.navbar-shell-premium {
    min-height: 78px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.25rem;
    padding: 0.85rem 1.15rem;
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid rgba(255, 255, 255, 0.55);
    box-shadow:
        0 12px 34px rgba(15, 23, 42, 0.10),
        0 2px 10px rgba(15, 23, 42, 0.05);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
}

.navbar-brand-premium {
    display: inline-flex;
    align-items: center;
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: #0f172a !important;
    text-decoration: none;
    margin: 0;
    line-height: 1;
}

.brand-main {
    color: #0f172a;
}

.brand-accent {
    color: #2563eb;
}

.navbar-right-premium {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-left: auto;
}

.navbar-links-premium {
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.nav-link-premium {
    color: #334155 !important;
    font-weight: 600;
    font-size: 1rem;
    padding: 0.65rem 0.95rem !important;
    border-radius: 999px;
    transition:
        background-color 0.25s ease,
        color 0.25s ease,
        transform 0.25s ease;
}

.nav-link-premium:hover,
.nav-link-premium:focus {
    color: #0f172a !important;
    background: rgba(15, 23, 42, 0.06);
    transform: translateY(-1px);
}

.navbar-actions-premium {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-left: 0.4rem;
}

.navbar-btn {
    min-height: 48px;
    border-radius: 999px;
    padding: 0.8rem 1.25rem;
    font-weight: 700;
    font-size: 0.98rem;
    border-width: 1px;
    transition:
        transform 0.28s ease,
        box-shadow 0.28s ease,
        background-color 0.28s ease,
        border-color 0.28s ease,
        color 0.28s ease;
}

.navbar-btn:hover,
.navbar-btn:focus {
    transform: translateY(-1px);
}

.navbar-btn-ghost {
    background: rgba(255, 255, 255, 0.42);
    border: 1px solid rgba(15, 23, 42, 0.10);
    color: #0f172a;
}

.navbar-btn-ghost:hover,
.navbar-btn-ghost:focus {
    background: rgba(255, 255, 255, 0.70);
    border-color: rgba(15, 23, 42, 0.16);
    color: #0f172a;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
}

.navbar-btn-primary {
    background: #0f172a;
    border: 1px solid #0f172a;
    color: #ffffff;
    box-shadow: 0 12px 26px rgba(15, 23, 42, 0.18);
}

.navbar-btn-primary:hover,
.navbar-btn-primary:focus {
    background: #111c33;
    border-color: #111c33;
    color: #ffffff;
    box-shadow: 0 16px 30px rgba(15, 23, 42, 0.22);
}

.navbar-mobile-toggle {
    min-height: 46px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.52);
    border: 1px solid rgba(15, 23, 42, 0.12);
    color: #0f172a;
    font-weight: 700;
    padding: 0.75rem 1rem;
    box-shadow: none;
}

.navbar-mobile-toggle:hover,
.navbar-mobile-toggle:focus {
    background: rgba(255, 255, 255, 0.74);
    border-color: rgba(15, 23, 42, 0.18);
    color: #0f172a;
}

#navbar-mobile-collapse {
    pointer-events: auto;
}

.navbar-mobile-panel {
    margin-top: 0.75rem;
    padding: 1rem;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(255, 255, 255, 0.58);
    box-shadow:
        0 16px 40px rgba(15, 23, 42, 0.12),
        0 2px 10px rgba(15, 23, 42, 0.05);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
}

.nav-link-mobile {
    display: block;
    color: #0f172a !important;
    font-weight: 600;
    font-size: 1rem;
    padding: 0.9rem 0.35rem !important;
    border-bottom: 1px solid rgba(15, 23, 42, 0.06);
    text-decoration: none;
}

.nav-link-mobile:last-of-type {
    border-bottom: none;
}

.navbar-mobile-actions {
    display: grid;
    gap: 0.75rem;
    margin-top: 1rem;
}

@media (max-width: 991.98px) {
    .site-navbar-wrap {
        padding-top: 0.85rem;
    }

    .navbar-shell-premium {
        min-height: 72px;
        padding: 0.8rem 1rem;
        border-radius: 20px;
    }

    .navbar-brand-premium {
        font-size: 1.45rem;
    }
}

@media (max-width: 575.98px) {
    .site-navbar-wrap {
        padding-top: 0.7rem;
    }

    .navbar-shell-premium {
        min-height: 68px;
        padding: 0.7rem 0.85rem;
        border-radius: 18px;
    }

    .navbar-brand-premium {
        font-size: 1.3rem;
    }

    .navbar-mobile-panel {
        border-radius: 18px;
        padding: 0.9rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    .nav-link-premium,
    .navbar-btn,
    .navbar-mobile-toggle {
        transition: none !important;
        transform: none !important;
    }
}

from unified_platform.registry import Module


def load_default_modules() -> list[Module]:
    return [
        Module(
            key="seo_audit",
            name="Audit SEO automatique",
            description="Analyse technique + recommandations.",
            category="acquisition",
        ),
        Module(
            key="seo_briefs",
            name="Générateur de briefs SEO",
            description="Mots-clés, intention, plan d'article.",
            category="acquisition",
        ),
        Module(
            key="editorial_calendar",
            name="Planification éditoriale",
            description="Calendrier de contenus.",
            category="acquisition",
        ),
        Module(
            key="title_hooks",
            name="Générateur de titres & hooks",
            description="Titres pour blogs et réseaux.",
            category="acquisition",
        ),
        Module(
            key="content_gap",
            name="Analyse concurrentielle de contenu",
            description="Top pages, gaps, opportunités.",
            category="acquisition",
        ),
        Module(
            key="rank_tracking",
            name="Suivi de positions SEO",
            description="Rangs, évolutions, alertes.",
            category="acquisition",
        ),
        Module(
            key="core_web_vitals",
            name="Analyse vitesse & Core Web Vitals",
            description="Diagnostic et actions prioritaires.",
            category="conversion",
        ),
        Module(
            key="onpage_optimization",
            name="Optimisation on-page",
            description="Checklist par URL.",
            category="conversion",
        ),
        Module(
            key="faq_generator",
            name="Générateur de FAQ",
            description="Questions SEO + schema.",
            category="conversion",
        ),
        Module(
            key="meta_descriptions",
            name="Générateur de meta-descriptions",
            description="Meta par page.",
            category="conversion",
        ),
        Module(
            key="visual_briefs",
            name="Générateur d'images/briefs visuels",
            description="Prompts + styles.",
            category="conversion",
        ),
        Module(
            key="social_posts",
            name="Rédaction de posts réseaux sociaux",
            description="Multi-formats.",
            category="conversion",
        ),
        Module(
            key="multichannel_distribution",
            name="Plan de diffusion multi-canal",
            description="Email + social + blog.",
            category="conversion",
        ),
        Module(
            key="content_performance",
            name="Analyse de performance de contenu",
            description="CTR, durée, conversions.",
            category="conversion",
        ),
        Module(
            key="industry_news",
            name="Veille d'actualités sectorielles",
            description="Alertes hebdomadaires.",
            category="retention",
        ),
        Module(
            key="landing_page_generator",
            name="Générateur de landing pages",
            description="Sections + copy.",
            category="conversion",
        ),
        Module(
            key="ab_testing_titles",
            name="A/B testing des titres",
            description="Suggestions + scoring.",
            category="conversion",
        ),
        Module(
            key="email_sequences",
            name="Générateur d'emails marketing",
            description="Séquences automatisées.",
            category="retention",
        ),
        Module(
            key="ads_analysis",
            name="Analyse de campagnes publicitaires",
            description="Résumé + actions.",
            category="acquisition",
        ),
        Module(
            key="audience_segmentation",
            name="Segmentation d'audience",
            description="Personas + messages.",
            category="retention",
        ),
        Module(
            key="roi_calculator",
            name="Calculateur ROI marketing",
            description="Budget, CAC, LTV.",
            category="retention",
        ),
        Module(
            key="kpi_dashboard",
            name="Dashboard KPIs marketing",
            description="MRR, CAC, churn.",
            category="retention",
        ),
        Module(
            key="light_crm",
            name="CRM léger",
            description="Suivi des leads.",
            category="retention",
        ),
        Module(
            key="offer_generator",
            name="Générateur d'offres & propositions commerciales",
            description="Templates structurés.",
            category="retention",
        ),
        Module(
            key="support_assistant",
            name="Assistant de support client",
            description="FAQ + réponses type.",
            category="retention",
        ),
    ]

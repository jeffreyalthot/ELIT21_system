from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class ModuleInfo:
    module_id: str
    name: str
    description: str
    category: str


MODULES: List[ModuleInfo] = [
    ModuleInfo(
        module_id="seo_audit",
        name="Audit SEO automatique",
        description="Analyse technique et recommandations SEO.",
        category="acquisition",
    ),
    ModuleInfo(
        module_id="seo_briefs",
        name="Générateur de briefs SEO",
        description="Mots-clés, intent, plan d’article.",
        category="acquisition",
    ),
    ModuleInfo(
        module_id="content_calendar",
        name="Planification éditoriale",
        description="Calendrier de contenus multi-canal.",
        category="acquisition",
    ),
    ModuleInfo(
        module_id="title_hooks",
        name="Générateur de titres & hooks",
        description="Titres optimisés pour blogs et réseaux.",
        category="acquisition",
    ),
    ModuleInfo(
        module_id="content_competition",
        name="Analyse concurrentielle de contenu",
        description="Pages top et gaps éditoriaux.",
        category="acquisition",
    ),
    ModuleInfo(
        module_id="rank_tracking",
        name="Suivi de positions SEO",
        description="Rangs, tendances, alertes.",
        category="acquisition",
    ),
    ModuleInfo(
        module_id="web_vitals",
        name="Analyse vitesse & Core Web Vitals",
        description="Diagnostic technique et actions prioritaires.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="on_page",
        name="Optimisation on-page",
        description="Checklist par URL et recommandations.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="faq_generator",
        name="Générateur de FAQ",
        description="Questions SEO + schema markup.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="meta_descriptions",
        name="Générateur de meta-descriptions",
        description="Meta descriptions par page.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="visual_briefs",
        name="Générateur d’images/briefs visuels",
        description="Prompts et styles visuels.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="social_posts",
        name="Rédaction de posts réseaux sociaux",
        description="Formats courts et longs adaptés aux réseaux.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="multichannel_plan",
        name="Plan de diffusion multi-canal",
        description="Emailing, social, blog.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="content_performance",
        name="Analyse de performance de contenu",
        description="CTR, durée, conversions.",
        category="retention",
    ),
    ModuleInfo(
        module_id="news_monitoring",
        name="Veille d’actualités sectorielles",
        description="Alertes hebdomadaires ciblées.",
        category="retention",
    ),
    ModuleInfo(
        module_id="landing_builder",
        name="Générateur de landing pages",
        description="Sections clés et copywriting.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="title_ab_tests",
        name="A/B testing des titres",
        description="Suggestions et scoring.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="email_sequences",
        name="Générateur d’emails marketing",
        description="Séquences de nurturing et vente.",
        category="retention",
    ),
    ModuleInfo(
        module_id="ads_analysis",
        name="Analyse de campagnes publicitaires",
        description="Résumé, anomalies et actions.",
        category="acquisition",
    ),
    ModuleInfo(
        module_id="audience_segmentation",
        name="Segmentation d’audience",
        description="Personas, messages clés.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="roi_calculator",
        name="Calculateur ROI marketing",
        description="Budget, CAC, LTV.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="kpi_dashboard",
        name="Dashboard KPIs marketing",
        description="MRR, CAC, churn.",
        category="retention",
    ),
    ModuleInfo(
        module_id="light_crm",
        name="CRM léger",
        description="Suivi des leads et pipeline.",
        category="retention",
    ),
    ModuleInfo(
        module_id="proposal_builder",
        name="Générateur d’offres & propositions",
        description="Templates de propositions commerciales.",
        category="conversion",
    ),
    ModuleInfo(
        module_id="support_assistant",
        name="Assistant de support client",
        description="FAQ et réponses types.",
        category="retention",
    ),
]


def iter_modules() -> Iterable[ModuleInfo]:
    return list(MODULES)

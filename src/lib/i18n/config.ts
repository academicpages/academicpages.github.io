import type { I18nConfig, I18nRuntimeConfig } from '@/types/i18n';

const DEFAULT_LOCALE = 'en';

function normalizeLocaleCode(locale: string): string {
  return locale.trim().replace('_', '-').toLowerCase();
}

function uniqueLocales(locales: string[]): string[] {
  return Array.from(new Set(locales.map(normalizeLocaleCode).filter(Boolean)));
}

export function getRuntimeI18nConfig(i18n?: I18nConfig): I18nRuntimeConfig {
  const rawLocales = i18n?.locales && i18n.locales.length > 0 ? i18n.locales : [DEFAULT_LOCALE];
  const locales = uniqueLocales(rawLocales);

  const defaultLocale = locales.includes(normalizeLocaleCode(i18n?.default_locale || ''))
    ? normalizeLocaleCode(i18n?.default_locale || '')
    : locales[0] || DEFAULT_LOCALE;

  const fixedCandidate = normalizeLocaleCode(i18n?.fixed_locale || '');
  const fixedLocale = locales.includes(fixedCandidate) ? fixedCandidate : defaultLocale;

  const labels: Record<string, string> = {};
  for (const locale of locales) {
    labels[locale] = i18n?.labels?.[locale] || locale;
  }

  const enabled = i18n?.enabled ?? false;

  if (!enabled) {
    return {
      enabled: false,
      locales: [defaultLocale],
      defaultLocale,
      mode: 'fixed',
      fixedLocale: defaultLocale,
      persist: false,
      switcher: false,
      labels: {
        [defaultLocale]: labels[defaultLocale] || defaultLocale,
      },
    };
  }

  return {
    enabled: true,
    locales,
    defaultLocale,
    mode: i18n?.mode === 'fixed' ? 'fixed' : 'auto',
    fixedLocale,
    persist: i18n?.persist ?? true,
    switcher: i18n?.switcher ?? true,
    labels,
  };
}

export function matchLocale(candidate: string | null | undefined, locales: string[]): string | null {
  if (!candidate) return null;

  const normalized = normalizeLocaleCode(candidate);
  if (locales.includes(normalized)) {
    return normalized;
  }

  const languageOnly = normalized.split('-')[0];
  if (locales.includes(languageOnly)) {
    return languageOnly;
  }

  return null;
}

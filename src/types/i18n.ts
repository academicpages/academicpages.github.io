export type I18nMode = 'auto' | 'fixed';

export interface I18nConfig {
  enabled?: boolean;
  locales?: string[];
  default_locale?: string;
  mode?: I18nMode;
  fixed_locale?: string;
  persist?: boolean;
  switcher?: boolean;
  labels?: Record<string, string>;
}

export interface I18nRuntimeConfig {
  enabled: boolean;
  locales: string[];
  defaultLocale: string;
  mode: I18nMode;
  fixedLocale: string;
  persist: boolean;
  switcher: boolean;
  labels: Record<string, string>;
}

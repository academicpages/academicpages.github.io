'use client';

import { create } from 'zustand';
import { matchLocale } from '@/lib/i18n/config';
import type { I18nRuntimeConfig } from '@/types/i18n';

const LOCALE_STORAGE_KEY = 'locale-storage';

interface LocaleStore {
  locale: string;
  isReady: boolean;
  locales: string[];
  defaultLocale: string;
  persistSelection: boolean;
  initialize: (config: I18nRuntimeConfig) => void;
  setLocale: (locale: string) => void;
}

function updateDocumentLocale(locale: string) {
  const root = document.documentElement;
  root.lang = locale;
  root.setAttribute('data-locale', locale);
}

function readPersistedLocale(locales: string[]): string | null {
  try {
    const raw = localStorage.getItem(LOCALE_STORAGE_KEY);
    return matchLocale(raw, locales);
  } catch {
    return null;
  }
}

function writePersistedLocale(locale: string) {
  try {
    localStorage.setItem(LOCALE_STORAGE_KEY, locale);
  } catch {
    // ignore storage errors
  }
}

function clearPersistedLocale() {
  try {
    localStorage.removeItem(LOCALE_STORAGE_KEY);
  } catch {
    // ignore storage errors
  }
}

function resolveInitialLocale(config: I18nRuntimeConfig): string {
  if (!config.enabled) {
    return config.defaultLocale;
  }

  const bootLocale = matchLocale(document.documentElement.getAttribute('data-locale'), config.locales);
  if (bootLocale) {
    return bootLocale;
  }

  if (config.persist) {
    const persisted = readPersistedLocale(config.locales);
    if (persisted) {
      return persisted;
    }
  }

  if (config.mode === 'fixed') {
    return config.fixedLocale;
  }

  const browserLocale = matchLocale(navigator.language, config.locales);
  return browserLocale || config.defaultLocale;
}

export const useLocaleStore = create<LocaleStore>()((set, get) => ({
  locale: 'en',
  isReady: false,
  locales: ['en'],
  defaultLocale: 'en',
  persistSelection: true,

  initialize: (config: I18nRuntimeConfig) => {
    const initialLocale = resolveInitialLocale(config);

    set({
      locale: initialLocale,
      isReady: true,
      locales: config.locales,
      defaultLocale: config.defaultLocale,
      persistSelection: config.persist,
    });

    if (config.persist) {
      writePersistedLocale(initialLocale);
    } else {
      clearPersistedLocale();
    }

    updateDocumentLocale(initialLocale);
  },

  setLocale: (locale: string) => {
    const { locales, defaultLocale, persistSelection } = get();
    const nextLocale = matchLocale(locale, locales) || defaultLocale;

    set({ locale: nextLocale });

    if (persistSelection) {
      writePersistedLocale(nextLocale);
    } else {
      clearPersistedLocale();
    }

    updateDocumentLocale(nextLocale);
  },
}));

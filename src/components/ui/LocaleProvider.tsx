'use client';

import { useEffect } from 'react';
import type { ReactNode } from 'react';
import { useLocaleStore } from '@/lib/stores/localeStore';
import type { I18nRuntimeConfig } from '@/types/i18n';

interface LocaleProviderProps {
  config: I18nRuntimeConfig;
  children: ReactNode;
}

export function LocaleProvider({ config, children }: LocaleProviderProps) {
  const initialize = useLocaleStore((state) => state.initialize);

  useEffect(() => {
    initialize(config);
  }, [initialize, config]);

  return <>{children}</>;
}

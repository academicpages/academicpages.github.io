'use client';

import { getMessages } from '@/lib/i18n/messages';
import { useLocaleStore } from '@/lib/stores/localeStore';

export function useMessages() {
  const locale = useLocaleStore((state) => state.locale);
  return getMessages(locale);
}

import { api } from './client';

export interface MailSubscription {
  id: number;
  name: string;
  keywords: string[];
  media: string[];
  schedule: 'Daily' | 'Weekly';
  time: string;
  weekDay: string | null;
  emails: string[];
  active: boolean;
  created_at: string;
  updated_at: string;
  last_sent_at: string | null;
}

export interface MailSubscriptionInput {
  name: string;
  keywords: string[];
  media: string[];
  schedule: 'Daily' | 'Weekly';
  time: string;
  weekDay?: string | null;
  emails: string[];
  active?: boolean;
}

export interface DashboardMailScope {
  subscription_id: string;
  name: string;
  owner_email: string;
  recipients: string[];
  keywords: string[];
  companies: string[];
  brands: string[];
  aliases: Record<string, string[]>;
  disease_areas: string[];
  policy_topics: string[];
  media: string[];
  custom_sources: string[];
  forwarded_input_paths: string[];
  personas: string[];
  lookback_hours: number;
  delivery_mode: 'gmail_draft' | 'gmail_send' | 'preview_only' | string;
  schedule: 'Daily' | 'Weekly';
  time: string;
  week_day: string | null;
  active: boolean;
  include_top_ma_signals: boolean;
  include_user_keyword_watchlist: boolean;
  updated_at: string;
}

export interface MailScopeResponse {
  scope: DashboardMailScope;
  scope_path: string;
  index_path: string;
}

export interface MailSubListResponse {
  items: MailSubscription[];
  smtp_configured: boolean;
}

export interface TestSendResult {
  ok: boolean;
  mode: 'smtp' | 'dry-run' | 'none';
  recipients: string[];
  message?: string;
}

export async function listMailSubscriptions(): Promise<MailSubListResponse> {
  return api.get<MailSubListResponse>('/api/mail-subscriptions');
}

export async function createMailSubscription(input: MailSubscriptionInput): Promise<MailSubscription> {
  const r = await api.post<{ item: MailSubscription }>('/api/mail-subscriptions', input);
  return r.item;
}

export async function updateMailSubscription(
  id: number,
  patch: Partial<MailSubscriptionInput>,
): Promise<MailSubscription> {
  const r = await api.patch<{ item: MailSubscription }>(`/api/mail-subscriptions/${id}`, patch);
  return r.item;
}

export async function deleteMailSubscription(id: number): Promise<void> {
  await api.delete<{ ok: true }>(`/api/mail-subscriptions/${id}`);
}

export async function testSendMailSubscription(id: number): Promise<TestSendResult> {
  return api.post<TestSendResult>(`/api/mail-subscriptions/${id}/test-send`, {});
}

export interface MailPreview {
  subject: string;
  html: string;
  text: string;
}

export async function previewMailSubscription(id: number): Promise<MailPreview> {
  return api.post<MailPreview>(`/api/mail-subscriptions/${id}/preview`, {});
}

export async function exportMailSubscriptionScope(id: number): Promise<MailScopeResponse> {
  return api.get<MailScopeResponse>(`/api/mail-subscriptions/${id}/scope`);
}

export async function previewAdHoc(name: string, keywords: string[], media: string[]): Promise<MailPreview> {
  const q = new URLSearchParams({
    name: name || 'Daily Dossier',
    keywords: keywords.join(','),
    media: media.join(','),
    format: 'json',
  });
  return api.get<MailPreview>(`/api/mailing/preview?${q.toString()}`);
}

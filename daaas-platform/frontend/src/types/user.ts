export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  avatar?: string;
  is_email_verified: boolean;
  date_joined: string;
}

export interface Organization {
  id: string;
  name: string;
  slug: string;
  plan: string;
  member_count: number;
  created_at: string;
}

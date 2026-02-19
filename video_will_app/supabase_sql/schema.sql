create table if not exists vaults (
  id uuid primary key default gen_random_uuid(),
  owner_user_id text not null,
  title text default 'Mon coffre',
  created_at timestamptz not null default now()
);

create table if not exists beneficiaries (
  id uuid primary key default gen_random_uuid(),
  vault_id uuid not null references vaults(id) on delete cascade,
  email text not null,
  created_at timestamptz not null default now(),
  unique(vault_id, email)
);

create table if not exists videos (
  id uuid primary key default gen_random_uuid(),
  vault_id uuid not null references vaults(id) on delete cascade,
  title text,
  storage_path text not null,
  created_at timestamptz not null default now(),
  released boolean not null default false
);

create table if not exists access_tokens (
  id uuid primary key default gen_random_uuid(),
  video_id uuid not null references videos(id) on delete cascade,
  beneficiary_email text not null,
  token_hash text not null,
  expires_at timestamptz not null,
  created_at timestamptz not null default now(),
  used_at timestamptz
);

create index if not exists idx_access_tokens_hash on access_tokens(token_hash);

from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "is_staff" BOOL NOT NULL  DEFAULT False,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "last_login" TIMESTAMPTZ,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT '2023-07-09T21:02:00.661893',
    "updated_at" TIMESTAMPTZ,
    "password" VARCHAR(128) NOT NULL,
    "uuid" UUID NOT NULL UNIQUE,
    "email" VARCHAR(128) NOT NULL UNIQUE,
    "last_name" VARCHAR(128),
    "first_name" VARCHAR(128),
    "middle_name" VARCHAR(128)
);
CREATE INDEX IF NOT EXISTS "idx_user_uuid_863a0b" ON "user" ("uuid");
CREATE INDEX IF NOT EXISTS "idx_user_email_1b4f1c" ON "user" ("email");
CREATE TABLE IF NOT EXISTS "action" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(128) NOT NULL,
    "code" VARCHAR(128) NOT NULL
);
CREATE TABLE IF NOT EXISTS "object" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(128) NOT NULL,
    "code" VARCHAR(128) NOT NULL
);
CREATE TABLE IF NOT EXISTS "permission" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(128) NOT NULL,
    "action_id" INT NOT NULL REFERENCES "action" ("id") ON DELETE CASCADE,
    "object_id" INT NOT NULL REFERENCES "object" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "role" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(128) NOT NULL
);
CREATE TABLE IF NOT EXISTS "session" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "uuid" UUID NOT NULL UNIQUE,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT '2023-07-09T21:02:00.674412',
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_session_uuid_092ac2" ON "session" ("uuid");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "user_role" (
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "role_id" INT NOT NULL REFERENCES "role" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "role_permission" (
    "role_id" INT NOT NULL REFERENCES "role" ("id") ON DELETE CASCADE,
    "permission_id" INT NOT NULL REFERENCES "permission" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

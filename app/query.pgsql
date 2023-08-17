SELECT * FROM posts;

INSERT INTO posts (title, content)
VALUES 
    ('vim creator died', '3 august vim creator passed off'),
    ('I use Arch, btw', 'thats so coooool')
RETURNING *; 

UPDATE posts
SET title = 'new title',
    content = 'new content',
    published = true
WHERE id = 5
RETURNING *;


CREATE TABLE IF NOT EXISTS posts
(
    id serial,
    title CHARACTER VARYING NOT NULL,
    content CHARACTER VARYING NOT NULL,
    published BOOLEAN NOT NULL DEFAULT true,
    created_at timestamp with time zone NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id)
);

DELETE FROM posts
WHERE title LIKE 'so much%'

-- Users
SELECT * FROM users;

INSERT INTO users (email, password)
VALUES 
    ('email@gmail.com', '1234'),
    ('gmail@gmail.com', '12345'),
    ('test@gmail.com', '12flakjd4')
RETURNING *;

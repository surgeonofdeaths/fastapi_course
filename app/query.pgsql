SELECT * FROM posts;

INSERT INTO posts (title, content, owner_id)
VALUES 
    ('vim creator died', '3 august vim creator passed off', 17),
    ('I use Arch, btw', 'thats so coooool', 17)
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

DELETE FROM votes;

SELECT * FROM users;
SELECT * FROM posts;
SELECT * FROM votes;

CREATE TABLE IF NOT EXISTS votes (
    post_id INT NOT NULL ,
    user_id INT NOT NULL,
    vote_value INT NOT NULL CHECK (vote_value = 1 OR vote_value = -1) DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, post_id)
);
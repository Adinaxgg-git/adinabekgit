import psycopg2
from config import DB_CONFIG


def connect():
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )


def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INT REFERENCES players(id),
            score INT,
            level INT,
            played_at TIMESTAMP DEFAULT NOW()
        );
    """)

    conn.commit()
    conn.close()


def save_game(username, score, level):

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    player = cur.fetchone()

    if not player:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        player_id = cur.fetchone()[0]
    else:
        player_id = player[0]

    cur.execute("""
        INSERT INTO game_sessions(player_id, score, level)
        VALUES (%s, %s, %s)
    """, (player_id, score, level))

    conn.commit()
    conn.close()


def leaderboard():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level, g.played_at
        FROM game_sessions g
        JOIN players p ON p.id = g.player_id
        ORDER BY g.score DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    conn.close()

    return data


def personal_best(username):

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT MAX(score)
        FROM game_sessions g
        JOIN players p ON p.id = g.player_id
        WHERE p.username=%s
    """, (username,))

    res = cur.fetchone()[0]

    conn.close()
    return res if res else 0
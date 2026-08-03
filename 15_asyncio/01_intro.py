"""
Async Programming (asyncio)

Imagine you're at a restaurant.

❌ Synchronous:
- Order food
- Stand at the counter doing absolutely nothing
- Wait until it's ready
- Eat

You're wasting time while waiting.

✅ Asynchronous:
- Order food
- Sit with friends
- Talk
- Food arrives
- Eat

While the food was cooking, you were free to do something else.

Computers behave the same way.

When waiting for:
- Database queries
- API requests
- File downloads
- Redis
- OpenAI
- S3 uploads

The CPU usually has nothing to do.

Async lets Python work on other tasks while waiting.
"""

import time


# ------------------------------------------------------------
# Synchronous Example
# ------------------------------------------------------------
def make_coffee() -> None:
    print("Starting coffee...")
    time.sleep(3)  # blocks the whole program for 3 seconds
    print("Coffee is ready!")


print("Morning Routine")
make_coffee()
print("Now reading a book")
print()


# ------------------------------------------------------------
# What happened?
# ------------------------------------------------------------
# 0s → start coffee
# ... wait ... wait ... wait ...  (CPU idle)
# 3s → coffee ready
# then → read book
#
# For 3 whole seconds the program did NOTHING useful.


# ------------------------------------------------------------
# Backend intuition
# ------------------------------------------------------------
# GET /users/1
#   → ask PostgreSQL
#   → wait ~200ms  (CPU idle)
#   → return JSON
#
# Download image → wait seconds for network
# Same problem: waiting is not "working".


# ------------------------------------------------------------
# The problem — one waiter, one customer
# ------------------------------------------------------------
# User A waiting 300ms → User B arrives → "Sorry, I'm busy waiting"
# even though the CPU isn't calculating anything.


# ------------------------------------------------------------
# Why async exists — keep the CPU useful while waiting
# ------------------------------------------------------------
# Instead of:
#   A wait… A done → B wait… B done
#
# We want:
#   A waiting → serve B → serve C → A's response arrives → return A


# ------------------------------------------------------------
# Important misconception
# ------------------------------------------------------------
# Async does NOT make a 500ms DB query finish in 100ms.
# The wait still takes 500ms.
# Async improves concurrency: do other work during waits.
#
# Faster car     → faster execution
# Better multitasking → async


# ------------------------------------------------------------
# Real-world awaits (preview — syntax comes next)
# ------------------------------------------------------------
# await database.fetch_one(...)
# await redis.get(...)
# await client.responses.create(...)
# await websocket.receive_text()
# await file.read()
#
# Common theme: waiting on something OUTSIDE your process.


# ------------------------------------------------------------
# Today's goal
# ------------------------------------------------------------
# Understand WHY async exists.
# Syntax (async def / await) comes in 02_coroutines.py.


# ------------------------------------------------------------
# Mini Challenge — answers
# ------------------------------------------------------------
# 1. Why is time.sleep() considered "blocking"?
#    It pauses the entire thread. Nothing else in that program can run
#    until the sleep finishes — even unrelated work.
#
# 2. Does async make code faster? If not, what does it improve?
#    No — individual waits take the same time.
#    It improves concurrency: other tasks can progress while one waits.
#
# 3. Name five operations where async is useful.
#    - Database queries
#    - HTTP / API calls
#    - Redis / cache I/O
#    - File / S3 downloads & uploads
#    - WebSockets / long-lived network I/O

print("--- Mini Challenge answers ---")
print("1. time.sleep blocks the whole thread — nothing else can run.")
print("2. Async isn't faster waits; it improves concurrency during waits.")
print("3. DB, HTTP APIs, Redis, file/S3 I/O, WebSockets.")

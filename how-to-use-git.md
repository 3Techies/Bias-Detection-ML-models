You want Git and GitHub basics, with branches, pulls, pushes, and not the mystical nonsense people usually dump on beginners. Fine. Let’s do this cleanly and correctly, like adults who want the project to actually survive three people touching it.

I’ll assume:

* Git is installed
* You already have a GitHub account
* One repo for your project
* You’re working from the terminal, not clicking buttons like it’s 2009

---

## 0. One-time setup (do this once per machine)

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

**What this does:**
Tells Git who you are so your commits don’t look like they came from a haunted laptop.

---

## 1. Clone the repository (everyone does this)

One person creates the repo on GitHub. Everyone else clones it.

```bash
git clone https://github.com/ORG_NAME/REPO_NAME.git
cd REPO_NAME
```

**Explanation:**

* `git clone` downloads the entire project + history to your machine.
* You now have a local copy linked to the GitHub repo (called `origin`).

---

## 2. Understand branches (before you break things)

* `main` (or `master`) = stable code. Treat it like glass.
* Feature branches = where actual work happens.
* Never code directly on `main`. Ever. That’s how teams implode.

Check existing branches:

```bash
git branch
```

---

## 3. Create a new branch (for your feature)

```bash
git checkout -b feature-login
```

**Explanation:**

* `checkout` switches branches
* `-b` creates the branch if it doesn’t exist
* `feature-login` is just a name. Use something meaningful.

Now you are working **only** on this branch.

---

## 4. Make changes (the obvious part)

Edit files however you want. Git does not care until you tell it to care.

Check what you changed:

```bash
git status
```

**Explanation:**
Shows modified, new, and staged files. Read it. It’s trying to help.

---

## 5. Stage changes (choose what to commit)

Stage specific files:

```bash
git add file1.py file2.js
```

Stage everything (use carefully):

```bash
git add .
```

**Explanation:**
Staging = selecting what goes into the next commit.
Git does not auto-save your chaos.

---

## 6. Commit changes (checkpoint, not backup)

```bash
git commit -m "Add login form validation"
```

**Explanation:**

* A commit is a snapshot of staged changes.
* Message should explain **what** changed, not your emotional journey.

---

## 7. Push your branch to GitHub

```bash
git push origin feature-login
```

**Explanation:**

* Sends your branch to GitHub.
* Others can now see your work.
* This does NOT touch `main`.

First push might need:

```bash
git push -u origin feature-login
```

That `-u` just sets upstream so future pushes are shorter.

---

## 8. Pull latest changes (do this often)

Before starting work each day:

```bash
git checkout main
git pull origin main
```

**Explanation:**

* Updates your local `main` with changes from others.
* Prevents surprise conflicts later when Git decides to ruin your afternoon.

---

## 9. Update your feature branch with latest main

```bash
git checkout feature-login
git merge main
```

**Explanation:**

* Brings new changes from `main` into your branch.
* Fix conflicts here, not during final merge.

If conflicts happen, Git will tell you exactly where. Open the files, fix them, then:

```bash
git add .
git commit -m "Resolve merge conflicts"
```

---

## 10. Create a Pull Request (PR) on GitHub

This part happens on GitHub, not terminal:

* Base branch: `main`
* Compare branch: `feature-login`

**Explanation:**

* PR lets teammates review your code.
* This is where bugs are caught before production explodes.
* After approval, merge the PR.

---

## 11. After PR is merged, clean up

Update local main:

```bash
git checkout main
git pull origin main
```

Delete local branch:

```bash
git branch -d feature-login
```

Delete remote branch:

```bash
git push origin --delete feature-login
```

**Explanation:**
No one needs 47 dead branches cluttering the repo like digital fossils.

---

## 12. Daily workflow summary (tattoo this mentally)

```text
git checkout main
git pull origin main
git checkout -b feature-x
# work
git add .
git commit -m "Meaningful message"
git push origin feature-x
# PR -> review -> merge
```

---

## Common mistakes people insist on making anyway

* Working on `main` directly
* Not pulling before starting work
* Committing random garbage with messages like “final final fix”
* Panic-merging conflicts without reading them
* Treating GitHub like Google Drive

---

If you want next:

* Git rebase vs merge (the religious war)
* Conflict resolution step-by-step
* A clean branching strategy for small teams
* GitHub Issues + Projects workflow

Git is boring once it clicks. Until then, it feels like it’s personally judging you. That part never fully goes away.

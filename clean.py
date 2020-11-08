from github import Github
from sys import argv


def main(token):
    g = Github(token)
    user = g.get_user()
    for repo in user.get_repos():
        if user.id == repo.owner.id:
            print("Delete %s? [y/n]" % repo.full_name)
            print("url: %s", repo.html_url)
            print("fork: %s" % repo.fork)
            print("Description:")
            print(repo.description)
            if input() == 'y':
                repo.delete()
                print("Deleted %s 👋" % repo.full_name)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide an access token. python clean.py <token>")

    token = argv[1]
    main(token)

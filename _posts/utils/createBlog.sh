# create blog with current date at beginning of filename followed by arg
# ex: ./createBlog javaIsCool.md
touch `date -u +"%Y-%m-%d-"`$1


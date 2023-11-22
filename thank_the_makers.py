from langchain.llms import OpenAI

# Initialize the OpenAI model
llm = OpenAI(api_key="your_api_key") # Replace with your actual API key

def generate_personal_message(author, commits):
    """
    Generates a personal message for each author based on their commits.
    """
    prompt = f"Write a thank you message for an open source contributor named {author}. " \
             f"They have made {commits} significant contributions including bug fixes, feature additions, " \
             f"and code optimizations."

    response = llm.complete(prompt, max_tokens=60)
    return response

def main():
    authors = get_commit_authors()
    author_count = collections.Counter(authors)

    # Sort authors by number of commits
    sorted_authors = sorted(author_count.items(), key=lambda x: x[1], reverse=True)

    # Update the THANKYOU file
    with open("THANKYOU.md", "w") as file:
        file.write("# Thank You Contributors!\n\n")
        file.write("Special thanks to our top contributors:\n\n")
        for author, count in sorted_authors:
            personal_message = generate_personal_message(author, count)
            file.write(f"- **{author}**: {count} commits. {personal_message}\n")

    print("THANKYOU file updated with top contributors and personalized messages.")

if __name__ == "__main__":
    main()

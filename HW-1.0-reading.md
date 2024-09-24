# HW-1: Background reading 

**Author(s)**: Dr. H and Gerrard Pendleton Thurston the 4th

Start the assignment by reading the following "back-ground" information, and reviewing the starter code.

`Don't worry`, most future assignments won't have this much reading, but since it is your first DSAN assignment, there is a little extra information that I'd like to communicate.

# Some Comments on Professionalism

## Importance of self education

* There are many steps in this assignment, we won't be covering everyone of them  in class, if you don't know how to do one of these steps, then please start by `trying to teach yourself`, e.g. reviewing shared codes and notes, or by Googling (or using Chat-GPT), for example by searching `How to load an image as a torch tensor in python`. 
  * That being said, excessive reliance on ChatGPT for coding tasks is neither acceptable nor advisable. Using it too often is akin to riding a bike with training wheels—eventually, those training wheels will come off. Those who relied too heavily on "training wheels" will `struggle and "crash"`. It's essential to develop your skills independently to ensure long-term success and competence.
* Self-education in data science is crucial due to the field's rapid evolution. Staying current with new tools, techniques, and trends enhances problem-solving skills, and adaptability. Continuous learning fosters innovation, sharpens critical thinking, and empowers individuals to tackle complex data challenges
  * Generally, a lack of independence or initiative to learn on your own is not a strength. Perhaps the last phrase you want to hear on the job is: "Would you like me to Google that for you?"

`Teach your class-mates`: 

One of the `best ways to learn` something new, is to pretend you need to `teach it` to someone else.

Your classmates are your friends and professional colleagues. If you know a concept or skill that one of your class mates doesn't, then consider `investing` the time to teach them. This not only helps them but also strengthens your professional network, making it a "win-win" situation. 

A rising tide raises all ships. By helping your classmates, you not only contribute to their success but also enhance the collective growth and prestige of the DSAN community and future alumni, benefiting everyone, including yourself.

### Note-taking 

Another way to reinforce your understanding of a topic is by taking detailed notes or working on **writing a book**, even if you never intend to share it with anyone. If you decide to write notes, then `Quarto` is an excellent tool for taking technical notes that involve mathematics, images, and computer code.

I've been taking digital notes for almost 15 years and have used many many different methods, including digitally-handwritten notes as well as textual notes. While you should use what works best for you, here’s my preferred tool stack for note-taking and other professional tools:

- **Document publishing:** `Quarto` or `LaTeX` (`Quarto` preferred)
- **Plaintext formatting:** `Markdown`
- **Quick image editing:** `Apple Keynote`
- **Mathematics typesetting (writing professional equations):** `LaTeX`
- **Markdown editing:** `VS Code` or `Typora`
- **OCR for equations and tables:** `Mathpix`
- **Citation management:** `BibTeX`
- **Website, note, book, and presentation creation:** `Quarto`
- **PDF document organization (managing your digital library):** `Zotero` (or `Mendeley`)
- **Proofreading, text summarization, idea generation, writing acceleration**: `chatGPT`
- **Screen reader:**
  - `Mac accessibility settings` → `Alt` + `Esc`
  - `Natural Reader` (naturalreader.com) and various smartphone apps also work well.

A screen reader can significantly boost productivity by enabling multitasking, reducing eye strain, and offering alternative ways to consume written content efficiently. 

*I guarantee that listening to your writing before submission will improve it significantly.*

## A note on writing with chatGPT 

Good writing typically `clearly` communicates the `authors desired message` in the `fewest possible number of words`. 

I use ChatGPT to improve and speed up my writing, but I still review and refine it until it's "pruned," "polished," and conveys exactly what I intend. Typically I read over a newly written paragraph over and over again, until I feel it is "polished" and flows well. 

Using ChatGPT outputs without careful editing and pruning can lead to an "information dump" that sounds boring and robotic—because, of course, it is. 

*Generally poor writing will NOT impress your reader, and will NOT make them think more highly of you.* 

Here are some useful and legitimate use-cases for writing with ChatGPT

* "In a concise bulleted list, describe X"
* "In a bulleted list, describe X in detail"
* "In 40 words, provide and overview of X"
* "Proof-read the following"  --> insert text 
* "Reword the following"  --> insert text 
* "clean this up" --> insert text 
* "Rewrite the following so that it is 50% shorter"  --> insert text 
* "Rewrite the following in 100 words"   --> insert text 
* "Summarize the following in a concise bulleted list"  --> insert text 

`IMPORTANT`: If the text you are inputting to ChatGPT for transformation is NOT ORIGINALLY YOUR OWN content, then you MUST cite the transformed text to provide attribution to the original creator. 

`Recommended reading:` To improve your writing, consider reading "On writing" By Stephen King, and "The Elements of Style" by Strunk and White

## Strive for excellence in your work

You should always strive to be the best professional version of yourself by giving 100% of your talent and skills to your work, even when you don’t feel like it. Striving for excellence ensures high-quality results, builds a strong reputation for both you and your colleagues, fosters personal and professional growth, and inspires confidence in others. Being the person who consistently delivers high-quality work quickly, with minimal oversight, will make you the "go-to" person for your boss for important tasks. This puts you on their radar, making you first in line for promotions, and last in line for layoffs. If the company or institution can’t function smoothly without you, then you’re unlikely to be let go.

Laziness, cheating, disorganization, and sloppy work are forms of disrespect to your colleagues. Time is one of the most valuable assets a person has. Doing sloppy or unprofessional work wastes others' time. Even worse, submitting sloppy work, with the expectation that someone else will clean up your mess is one of the worst ways to show disregard for them.

## Back-up your work

Your code should always be backed up to the cloud, ideally with multiple redundancies. Keeping your working directory inside a cloud drive on your laptop (e.g., Google Drive, OneDrive, Box, Dropbox, iCloud, etc) is a great practice. Additionally, you should regularly commit and push your code to GitHub, ensuring you have multiple cloud backups, as well as a local version, in case of accidental deletion. I've tried most the the cloud services over the years; while they all have their quirks, I find Dropbox to be the most robust and reliable, causing the least headaches.


# Useful reference 

## Relevant notes

There is some useful starter code and documentation in the links below. Please start the assignment by reviewing them. 

* https://jfh.georgetown.domains/centralized-lecture-content/content/computer-science/python/creating-a-python-package/notes.html
* https://jfh.georgetown.domains/centralized-lecture-content/content/computer-science/python/object-and-classes/demo.html
* https://jfh.georgetown.domains/centralized-lecture-content/content/machine-learning/computer-vision/fundamentals/overview-of-image-data/notes.html
* https://jfh.georgetown.domains/centralized-lecture-content/content/mathematics/calculus/fundamentals/calculus-overview/notes.html

## Python naming conventions

Please adhere to the following Python naming conventions:

1. **Variables/Functions**: Use `snake_case` (lowercase with underscores).  
2. **Classes**: Use `CamelCase` (capitalize each word).  
3. **Constants**: Use `ALL_CAPS_WITH_UNDERSCORES`.
4. **Modules/Packages**: Use lowercase with underscores if needed.
5. **Private Attributes**: Prefix with a single underscore (`_name`).
6. **Built-in Overrides**: Avoid using names that clash with Python’s built-in functions or modules.

These conventions help maintain readability and consistency in Python code.

## Hidden files

A hidden file (or folder) in Linux or macOS is a file that is not displayed by default in file listings. It is identified by a leading dot `.` and is used for configuration or system settings (e.g., `.config` or `.git`), making it "hidden."

You can see hidden files with`ls -a`  where the `-a` flag stands for "all"

A common example is the `.gitignore` file which specifies which files or directories Git should ignore, preventing them from being tracked or committed. It's used to exclude sensitive data, build files, and store temporary files.

## Warning: Deleting Files Using Scripts

The following commands delete files (there are similar versions in python)

* Delete a file: `rm file_name` 
* Delete a folder: `rm -fr folder_name` 

Deleting files via scripts can be risky and irreversible. Always proceed with caution 

1. **Backup First**: Ensure all important data is backed up before running deletion scripts.
2. **ALWAYS specify the exact filename** you want to delete, for example `rm website/pages/processing-log.qmd`
3. **NEVER NEVER NEVER use a wild-card**  in a delete command, e.g. `rm -rf *` will irreversibly delete the entire directory tree starting from the current working directory (CWD).
   1. **If you run this from the wrong directory you can irreversibly delete everything on the computer's disk, including the operating system and all files**
4. **Test in a Safe Environment**: Run the script in a non-critical environment or on a subset of files to verify it works as expected.
5. **Dry Run Option**: Include a "dry run" mode that simulates the deletion without actually removing files.
6. **Review Scripts Regularly**: Periodically review and test deletion scripts to ensure they are still accurate and safe.

Mistakes can be costly, so always double-check before running any script that deletes files.

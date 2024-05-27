# chunkify
# @g3jerrie

Script / Tool for Large File Chunking and Merging

The proposed tool facilitates the efficient handling of large files by splitting them into smaller chunks  using the 'chunkster.py'. These chunks can then be uploaded to cloud storage services or shared via Instant Messaging (IM) apps. This approach is particularly useful in scenarios where there are size limits on individual files. Subsequently, the recipient can download the chunks to their destination system and merge them seamlessly using the ‘mergester.py’.

Use Cases:

Telegram: When using Telegram, the tool allows users to send large files (such as .zip archives) in manageable chunks. Telegram imposes a maximum file size limit (e.g., 2GB or 4GB), so breaking down the file ensures successful transmission. Upon receipt, the recipient can merge the chunks into the complete file on their local machine.

Git Repositories: In software development, Git repositories often contain resource files that exceed the recommended file size for efficient version control. By employing our tool, developers can store large resource files directly within the project repository. During the build generation process, these chunks can be merged into the complete resource file, ensuring seamless integration.

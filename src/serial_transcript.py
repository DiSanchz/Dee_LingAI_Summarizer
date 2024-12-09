import whisper
import os


class WhisperTranscriber:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.reccordings = {}

    def check_target_dir(self):
        """
        Check if the provided target directory exists.
        """
        if not os.path.isdir(self.target_dir):
            print("Target directory does not exist")
            return False
        else:
            return

    def scan_for_reccordings(self):
        """
        Scan the target directory for audio reccordings.
        """
        files = os.listdir(self.target_dir)
        self.reccordings = {}

        for i in range(len(files)):
            filename = files[i]
            if filename.endswith((".mp3", ".mp4")):
                reccording_full_path = os.path.join(self.target_dir, filename)
                reccording_name = filename.split(".")[0]

                self.reccordings[i] = {
                    "reccording_name": reccording_name,
                    "reccording_full_path": reccording_full_path,
                }

    def transcribe_audio(self, model="medium.en"):
        """
        Transcribe audio recordings using the specified model and save the
        transcripts at self.target_directory/transcrips.
        """

        transcriber = whisper.load_model(model)

        if not os.path.exists(f"{self.target_dir}/transcripts"):
            os.makedirs(f"{self.target_dir}/transcripts")

        for key, value in self.reccordings.items():
            transcript = transcriber.transcribe(
                self.reccordings[key]["reccording_full_path"]
            )

            with open(
                f"{self.target_dir}/transcripts/transcript_{self.reccordings[key]['reccording_name']}.txt",
                "w",
            ) as file:
                file.write(transcript["text"])

            print(f"Transcript {self.reccordings[key]['reccording_name']}: Ready")

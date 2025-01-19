class Logger:
    def __init__(self):
        self.matches = []
        self.mismatches = []

    def log_match(self, lr_img, hr_img, metrics):
        self.matches.append({
            'LR': lr_img,
            'HR': hr_img,
            'metrics': metrics
        })

    def log_mismatch(self, lr_img, hr_img, metrics):
        self.mismatches.append({
            'LR': lr_img,
            'HR': hr_img,
            'metrics': metrics
        })

    def save_log(self):
        with open('log.txt', 'w') as file:
            file.write("Matches:\n")
            for match in self.matches:
                file.write(f"LR: {match['LR']} | HR: {match['HR']} | Metrics: {match['metrics']}\n")

            file.write("\nMismatches:\n")
            for mismatch in self.mismatches:
                file.write(f"LR: {mismatch['LR']} | HR: {mismatch['HR']} | Metrics: {mismatch['metrics']}\n")

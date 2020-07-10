var Environments = {
    "DEBUG": "DEBUG",
    "RELEASE": "RELEASE"
};

class Settings {

    Environment = null;

    SetEnvironment(environment) {
        switch (environment) {
            case "DEBUG":
                this.Environment = Environments.DEBUG;
                break;
            case "RELEASE":
            case "CANDIDATE_TO_RELEASE":
                this.Environment = Environments.RELEASE;
                break;
        }
    }

}

var ProjectSettings = new Settings();
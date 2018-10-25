import lib
import json

class UserExport():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.csv_writer = lib.CsvWriter()
        self.rl_sess = lib.RLSession(self.config.rl_user,self.config.rl_pass,self.config.rl_cust)
        self.output = [["displayName", "email", "enabled", "firstName", "lastName", "roleType"]]

    def build(self):
        self.url = "https://api.redlock.io/user"
        self.rl_sess.authenticate_client()
        response = self.rl_sess.client.get(self.url)
        #write out the top of csv to file
        self.csv_writer.write(self.output)
        json_response = response.json()
        for userdata in json_response:
            data = [userdata["displayName"],userdata["email"],userdata["enabled"],userdata["firstName"],userdata["lastName"],userdata["roleType"]]
            self.csv_writer.append([data])

    def run(self):
        self.build()

def main():
    rl_userexport = UserExport()
    rl_userexport.run()


if __name__ == "__main__":
    main()

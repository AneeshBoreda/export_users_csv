import lib
import json

class UserExport():
    def __init__(self):
        self.config = lib.ConfigHelper()
        self.csv_writer = lib.CsvWriter()
        self.rl_sess = lib.RLSession(self.config.rl_user,self.config.rl_pass,self.config.rl_cust,self.config.rl_api_base)
        self.output = [["displayName", "email", "enabled", "firstName", "lastName", "roleType", "groupIds"]]

    def build(self):
        self.url = "https://" + self.config.rl_api_base + "/user"
        self.rl_sess.authenticate_client()
        users = self.rl_sess.client.get(self.url)
        self.url = "https://" + self.config.rl_api_base + "/user/role"
        roles = self.rl_sess.client.get(self.url)
        #write out the top of csv to file
        self.csv_writer.write(self.output)
        json_users = users.json()
        json_roles = roles.json()
        user_group = []
        for role in json_roles:
            if not role['associatedUsers']:
                continue
            else:
                groupid = role['accountGroupIds']
                for user in role['associatedUsers']:
                    data = {"username": user, "groups": groupid}
                user_group.append(data)


        for userdata in json_users:
            for user in user_group:
                if userdata['email'] == user['username']:
                    data = [userdata["displayName"],userdata["email"],userdata["enabled"],userdata["firstName"],userdata["lastName"],userdata["roleType"],str(user["groups"])[1:-1]]
                    self.csv_writer.append([data])


    def run(self):
        self.build()

def main():
    rl_userexport = UserExport()
    rl_userexport.run()


if __name__ == "__main__":
    main()

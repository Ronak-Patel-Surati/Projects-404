import { ID, Account, Client } from "appwrite";
import Var from "@env";
// //
// console.log(APPWRITE_ENDPOINT); // Should print the endpoint
// console.log(APPWRITE_PROJECT_ID); // Should print the project ID

const AppWriteClient = new Client();

const APPWRITE_ENDPOINT: string = Var.APPWRITE_ENDPOINT!;
const APPWRITE_PROJECT_ID: string = Var.APPWRITE_PROJECT_ID!;

type CreateUserAccount = {
  email: string;
  password: string;
  name: string;
};

type LoginUserAccount = {
  email: string;
  password: string;
};

class AppWriteService {
  account;

  constructor() {
    AppWriteClient.setEndpoint(APPWRITE_ENDPOINT).setProject(
      APPWRITE_PROJECT_ID
    );

    this.account = new Account(AppWriteClient);
  }
  //Creating a new recode of user inside of appwrite
  async createAccount({ email, password, name }: CreateUserAccount) {
    try {
      const userAccount = await this.account.create(
        ID.unique(),
        email,
        password,
        name
      );
      if (userAccount) {
        //login setup
        return this.login({ email, password });
      }
    } catch (error) {
      console.log(error);
    }
  }
  async login({ email, password }: LoginUserAccount) {
    try {
      return await this.account.createEmailPasswordSession(email, password);
    } catch (error) {
      console.log(error);
    }
  }
  async getCurrentUser() {
    try {
      return await this.account.get();
    } catch (error) {
      console.log(error);
    }
  }
  async logout() {
    try {
      return await this.account.deleteSession("current");
    } catch (error) {
      console.log(error);
    }
  }
}
export default AppWriteService;

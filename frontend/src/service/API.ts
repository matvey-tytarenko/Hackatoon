import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:5000";

export default () => {
  return {
    createSession: async function () {
      try {
        const res = await axios.get("/get_ticket", {});

        // debugger;
        const ticketnumber = res.data.message;
        console.log(ticketnumber);
        return ticketnumber;
      } catch (err) {
        //debugger;
      }
    },
    askQuestion: async function (question: string) {
      const res = await axios.post("/ask", {
        question: question,
      });
      return res.data.message;
    },
  };
};

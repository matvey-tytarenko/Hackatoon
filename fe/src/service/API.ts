import axios from "axios";

const ip = " https://api.danihek.xyz/get_ticket";
export default () => {
  return {
    createSession: async function () {
      const res = await axios.post(ip, {});
      const ticketnumber = res.data.ticket_number;
      console.log(ticketnumber);
      return ticketnumber;
    },
    // askQuestion: async function (ticketnumber, question) {
    //   const res = await axios.post("http://10.250.160.78:3000/ask", {
    //     ticket_number: ticketnumber,
    //     question: question,
    //   });
    //   return res.data;
    // },
  };
};

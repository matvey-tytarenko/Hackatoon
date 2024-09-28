import axios from "axios";

const api_endpoint = "";
export default () => {
  return {
    createSession: async function () {
      // const res = await axios.post('localhost:8080/create_session', {  });
      // const ticketnumber = res.token
      const ticketNumber = 123;
      return ticketNumber;
      
    },
  };
};

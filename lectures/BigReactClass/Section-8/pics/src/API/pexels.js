import axios from "axios";

export default axios.create({
    baseURL: "https://api.pexels.com/v1/",
    headers: {
        Authorization: '563492ad6f91700001000001ae7afc5423cd4f93a8c76c5823d2b728'
    }
});
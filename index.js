const { GoogleGenerativeAI } = require("@google/generative-ai");

const genAI = new GoogleGenerativeAI("AIzaSyBYO8bvnvgPQ3w4hYS2C4xFOpS2-sBDT94");

const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
const prompt = "Halo Apa Kabar?";
// const image = {
  // inlineData: {
    // data: Buffer.from(fs.readFileSync("cookie.png")).toString("base64"),
    // mimeType: "image/png",
  // },
// };

const result = await model.generateContent([prompt]);
console.log(result.response.text())
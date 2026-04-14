export default function handler(req, res) {
  // method check (GET/POST dono handle kar sakte hain)
  if (req.method === "GET") {
    return res.status(200).json({
      message: "Vercel API is working 🚀"
    });
  }

  if (req.method === "POST") {
    const { message } = req.body;

    return res.status(200).json({
      reply: `You said: ${message}`
    });
  }

  return res.status(405).json({
    error: "Method not allowed"
  });
}

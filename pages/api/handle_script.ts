// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'

type Data = {
  message: string
}

export default function handler(req: NextApiRequest, res: NextApiResponse<Data>) {
  const execSync = require('child_process').execSync
  const pythonProcess = execSync('python pages/api/get_players.py')
  console.log('working here')
  console.log(pythonProcess.toString())
  return res.json({ message: pythonProcess.toString() });
}
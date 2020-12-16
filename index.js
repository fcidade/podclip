const robots = {
  userInput: require('./robots/user-input'),
  text: require('./robots/text-robot'),
}

async function start() {
  const content = {}

  robots.userInput(content)
  await robots.text(content) 

  console.log(content)
}

start()
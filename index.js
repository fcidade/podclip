const robots = {
  userInput: require('./robots/user-input'),
  text: require('./robots/text-robot'),
}

function start() {
  const content = {}

  robots.userInput(content)
  robots.text(content)

  console.log(content)
}

start()
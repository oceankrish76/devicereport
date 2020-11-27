// import other routes
const dataRoutes = require('./data')

const appRouter = (app, fs) => {

  // default route
  app.get('/', (req, res) => {
    res.send('welcome to the development api-server')
  })

  // other routes
  dataRoutes(app, fs)

}

module.exports = appRouter
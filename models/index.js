const { Sequelize } = require("sequelize");
const dbmsConfig = require("../config/dbms.config");
const dbConfig = require("../config/db.config");

// Création de l'instance Sequelize
const instance = new Sequelize(process.env.ENVIRONMENT === "prod" ? dbmsConfig : dbConfig);()

// Models
const models = {};


// // Associations
Object.keys(models).forEach((modelName) => {
  if (models[modelName].associate) {
    models[modelName].associate(models);
  }
});

// instance.sync({ force: true }).then(() => {
//   console.log("reset database success"); 
// });

instance.sync({ force: true }).then(() => {
  console.log("Base de données synchronisée (force true)");
}).catch((err) => {
  console.error("Erreur lors de la synchronisation de la base :", err);
});

module.exports = {
  instance,
  ...models,
};

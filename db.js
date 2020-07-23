const { Model, DataTypes, Sequelize } = require('sequelize');

const sequelize = new Sequelize('bf', 'root', '123456', {
    host: 'localhost',
    port: 3306,
    dialect: 'mysql'
});

class Keyword extends Model {}
class GoogleSERP extends Model {}

Keyword.init({
  // Model attributes are defined here
  id: {
    type: DataTypes.BIGINT,
    primaryKey: true,
    autoIncrement: true,
    allowNull: false
  },
  keyword: {
    type: DataTypes.STRING,
    allowNull: false
  },
  country: {
    type: DataTypes.STRING
    // allowNull defaults to true
  },
  type: {
    type: DataTypes.STRING
    // allowNull defaults to true
  }
}, {
  // Other model options go here
  sequelize, // We need to pass the connection instance
  modelName: 'Keyword', // We need to choose the model name
  tableName: 'keyword',
  timestamps: false
});

GoogleSERP.init({
    id: {
      type: DataTypes.BIGINT,
      primaryKey: true,
      autoIncrement: true,
      allowNull: false
    },
    keyword_id: {
        type: DataTypes.BIGINT,
        allowNull: false
      },
    keyword: {
      type: DataTypes.STRING,
      allowNull: false
    },
    rank: {
      type: DataTypes.BIGINT
    },
    link: {
      type: DataTypes.STRING
    },
    snippet: {
        type: DataTypes.STRING
    },
    title: {
        type: DataTypes.STRING
    },
    visible_link: {
        type: DataTypes.STRING
    },
  }, {
    // Other model options go here
    sequelize, // We need to pass the connection instance
    modelName: 'GoogleSERP', // We need to choose the model name
    tableName: 'google_serp_202007',
    timestamps: false
  });

(async () => {
    try {
        await sequelize.authenticate();
        console.log('Connection has been established successfully.');

        const keywords = await Keyword.findAll();
        // console.log("All keywords:", JSON.stringify(keywords, null, 2));

        const serp = await GoogleSERP.create({ keyword_id: 1, keyword: "test keyword", rank: 1, link: 'http://test.org', snippet: 'xxxx', title: 'test keyword title', visible_link: 'lll' });
        console.log("google serp's auto-generated ID:", serp.id);

      } catch (error) {
        console.error('Unable to connect to the database:', error);
    }
})()
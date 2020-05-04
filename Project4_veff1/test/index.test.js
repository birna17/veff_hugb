//Importing the application to test
let server = require('../index');
let mongoose = require("mongoose");
let Event = require('../models/event');
let Booking = require('../models/booking');

//These are the actual modules we use
let chai = require('chai');
let should = chai.should();
let chaiHttp = require('chai-http');
chai.use(chaiHttp);

describe('Endpoint tests', () => {
    //###########################
    //These variables contain the ids of the existing event/booking
    //That way, you can use them in your tests (e.g., to get all bookings for an event)
    //###########################
    let eventId = '';
    let bookingId = '';

    //###########################
    //The beforeEach function makes sure that before each test, 
    //there is exactly one event and one booking (for the existing event).
    //The ids of both are stored in eventId and bookingId
    //###########################
    beforeEach((done) => {
        let event = new Event({ name: "Test Event", capacity: 10, startDate: 1590840000000, endDate: 1590854400000});

        Event.deleteMany({}, (err) => {
            Booking.deleteMany({}, (err) => {
                event.save((err, ev) => {
                    let booking = new Booking({ eventId: ev._id, firstName: "Jane", lastName: "Doe", email: "jane@doe.com", spots: 2 });
                    booking.save((err, book) => {
                        eventId = ev._id;
                        bookingId = book._id;
                        done();
                    });
                });
            });
        });
    });

    //###########################
    //Write your tests below here
    //###########################

    it("GET /api/v1/events", function (done) {
        chai.request('http://localhost:3000')
            .get('/api/v1/events')
            .end( (err,res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.json;
                chai.expect(res.body).to.be.a('array');
                chai.expect(Object.keys(res.body).length).to.be.eql(1);
                done();
            });
    });

    it("GET /api/v1/events/:eventId", function (done) {
        chai.request('http://localhost:3000')
            .get('/api/v1/events/'+eventId)
            .end( (err,res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.json;
                chai.expect(res.body).to.have.property('description').eql('');
                chai.expect(res.body).to.have.property('location').eql('');
                chai.expect(res.body).to.have.property('name').eql('Test Event');
                chai.expect(res.body).to.have.property('capacity').eql(10);
                chai.expect(res.body).to.have.property('_id').eql(eventId.toString());
                chai.expect(res.body).to.have.property('bookings').to.be.a('array');
                chai.expect(Object.keys(res.body).length).to.be.eql(8);
                done();
            });
    });

    it("GET /api/v1/events/:eventId/bookings", function (done) {
        chai.request('http://localhost:3000')
            .get('/api/v1/events/'+eventId+'/bookings')
            .end( (err,res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.json;
                chai.expect(res.body).to.be.a('array');
                chai.expect(Object.keys(res.body).length).to.be.eql(1);
                done();
            });
    });

    it("GET /api/v1/events/:eventId/bookings/:bookingId", function (done) {
        chai.request('http://localhost:3000')
            .get('/api/v1/events/'+eventId+'/bookings/'+bookingId)
            .end( (err,res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.json;
                chai.expect(res.body).to.have.property('tel').eql('');
                chai.expect(res.body).to.have.property('email').eql('jane@doe.com');
                chai.expect(res.body).to.have.property('_id').eql(bookingId.toString());
                chai.expect(res.body).to.have.property('firstName').eql('Jane');
                chai.expect(res.body).to.have.property('lastName').eql('Doe');
                chai.expect(res.body).to.have.property('spots').eql(2);
                chai.expect(Object.keys(res.body).length).to.be.eql(6);
                done();
            });
    });


    it("POST /api/v1/events", function (done) {
        chai.request('http://localhost:3000')
        .post('/api/v1/events')
        .set('Content-type', 'application/json')
        .send({'description':'Útitónleikar', 'location':'Reykjavik', 'name':'Útitónleikar Gylfa',
        'capacity':50,'startDate':1985083078000 ,'endDate':19585083078000})
        .end( (err, res) => {
            chai.expect(res).to.have.status(201);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.have.property('description').eql('Útitónleikar');
            chai.expect(res.body).to.have.property('location').eql('Reykjavik');
            chai.expect(res.body).to.have.property('name').eql('Útitónleikar Gylfa');
            chai.expect(res.body).to.have.property('capacity').eql(50);
            chai.expect(res.body).to.have.property('_id');
            chai.expect(Object.keys(res.body).length).to.be.eql(7);
            done();
        });
    });

    it("POST /api/v1/events/:eventId/bookings", function (done) {
        chai.request('http://localhost:3000')
        .post('/api/v1/events/'+eventId+'/bookings/')
        .set('Content-type', 'application/json')
        .send({'tel':6669988, 'email':'gylfi@gylfi.is', 'firstName':'Gylfi',
        'lastName':'Gylfason','spots':5})
        .end( (err, res) => {
            chai.expect(res).to.have.status(201);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.have.property('tel').eql('6669988');
            chai.expect(res.body).to.have.property('email').eql('gylfi@gylfi.is');
            chai.expect(res.body).to.have.property('firstName').eql('Gylfi');
            chai.expect(res.body).to.have.property('lastName').eql('Gylfason');
            chai.expect(res.body).to.have.property('spots').eql(5);
            chai.expect(res.body).to.have.property('_id');
            chai.expect(Object.keys(res.body).length).to.be.eql(6);
            done();
        });
    });


    it("DELETE /api/v1/events/:eventId/bookings/:bookingId", function (done) {
        chai.request('http://localhost:3000')
        .delete('/api/v1/events/'+eventId+'/bookings/'+bookingId)
        // .auth('****', '****')
        .set({'Content-type':'application/json','Authorization':'Basic YWRtaW46c2VjcmV0'})
        .end( (err,res) => {
            chai.expect(res).to.have.status(200);
            done();
        });
    });

    it("DELETE /api/v1/events/:eventId/bookings/:bookingId failure case", function (done) {
        chai.request('http://localhost:3000')
        .delete('/api/v1/events/'+eventId+'/bookings/'+bookingId)
        // .auth('****', '123123')
        .set({'Content-type':'application/json','Authorization':'Basic Z3lsZmk6MTIzMTIz'})
        .end( (err,res) => {
            chai.expect(res).to.not.have.status(200);
            done();
        });
    });



});
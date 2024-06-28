import { createQueue } from 'kue';
import { expect } from 'chai';
import { spy } from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs tests', () => {
    const queue = createQueue();
    before(() => {
        queue.testMode.enter();
    });
    afterEach(() => {
        queue.testMode.clear();
    });
    after(() => {
        queue.testMode.exit();
    });
    
    it('display a error message if jobs is not an array', () => {
        const job = { phoneNumber: '1234567890', message: 'test message' };
        expect(() => createPushNotificationsJobs(job, queue)).to.throw('Jobs is not an array');
    });
    it('create two new jobs to the queue', () => {
        const consoleSpy = spy(console, 'log');        
        const jobs = [
            { phoneNumber: '1234567890', message: 'test message' },
            { phoneNumber: '2345678901', message: 'another test message' },
        ];
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(consoleSpy.calledTwice).to.be.true;
        expect(consoleSpy.firstCall.args[0]).to.equal(`Notification job created: ${queue.testMode.jobs[0].id}`);
    });
    it('test data added to the queue successfully', () => {
        const jobs = [{ phoneNumber: '1234567890', message: 'test message' }];
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
    });
});

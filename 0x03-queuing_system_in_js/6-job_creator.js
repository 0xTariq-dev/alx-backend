import { createQueue } from 'kue';

const queue = createQueue();
const jobData = {
    phoneNumber: '1234567890',
    message: `This is the code to verify your account: 1234 \nDon't share it with anyone.`
};

const job = queue.create('push_notification_code', jobData).save()

job
.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
.on('complete', () => console.log('Notification job completed'))
.on('failed', () => console.log('Notification job failed'));

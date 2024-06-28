function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
    jobs.forEach((job) => {
        const notification = queue.create('push_notification_code_3', job).save((err) => {
            if (!err) console.log(`Notification job created: ${notification.id}`);
        });
        const id = notification.id;
        notification
        .on('complete', () => console.log(`Notification job ${id} completed`))
        .on('failed', (err) => console.log(`Notification job ${id} failed: ${err}`))
        .on('progress', (progress) => console.log(`Notification job ${id} ${progress}% complete`));
    });
};

module.exports = createPushNotificationsJobs;

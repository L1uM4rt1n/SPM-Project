const show_all_jobs = 'http://localhost:5007/get_all_jobs';
axios.get(show_all_jobs)
    .then((response) => {
        console.log(response);
        const job_listings = response.data.job_listings;
        // create table for job listings
        const table = document.createElement('table');
        table.classList.add('table', 'table-bordered');

        table.innerHTML = `
            <thead class="thead-light">
                <tr>
                    <th>Job Title</th>
                    <th>Department</th>
                    <th>App Deadline</th>
                    <th>Skills Required</th>
                </tr>
            </thead>
            <tbody>
            </tbody>
        `;

        const tbody = table.querySelector('tbody');
        for (const jobListing of job_listings) {
            const tr = document.createElement('tr');

            // show only date for app_deadline
            const appDeadlineDate = new Date(jobListing.App_Deadline);
            const formattedAppDeadline = appDeadlineDate.toDateString();

            tr.innerHTML = `
                <td>${jobListing.Role_Name}</td>
                <td>${jobListing.Job_Department}</td>
                <td>${formattedAppDeadline}</td>
               
            `;
            tbody.appendChild(tr);
        }
        //  <td>${jobListing.Skills_req.join(', ')}</td>
        document.body.appendChild(table);
    })
    .catch((error) => {
        console.log(error);
    });
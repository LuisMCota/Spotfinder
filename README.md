# SpotFinder (Business Information Finder)
SpotFinder is a web application designed to assist users in finding general information about businesses within a specified area. By utilizing the "Places" API from Google Cloud, SpotFinder gathers relevant data on businesses around the user-specified location. This information can be instrumental in helping users assess the suitability of an area for starting a new business by identifying any potential issues or challenges.

## Features
- Business Information: SpotFinder provides users with essential information about businesses in the specified area, including their names, types, addresses, and contact details.
- Data Analysis: Users can download the gathered information from the web application to perform further analysis. This allows users to make informed decisions about whether to proceed with establishing a business in the chosen area.
-Google Cloud Integration: Leveraging the powerful "Places" API from Google Cloud ensures accurate and up-to-date business data for users.


## How to Use
- Specify Location: Enter the desired location or area for which you want to find business information.
- Retrieve Data: Click on the "Search" button to fetch data about businesses in the specified area.
- Analyze: Review the information provided, download the data if necessary, and analyze it to make informed decisions about potential business opportunities in the area.

## Technologies Used
- Frontend: HTML, CSS, Tailwind
- API: Google Cloud "Places" API
- Python
- Docker

# Getting Started
To get started with the SpotFinder web application, follow these steps:
-  Clone this repository to your local computer.
-  Install Docker.
- Set up your Docker account.
- Open your terminal, locate your folder and writer the following commands:
```cmd
docker build -t app-flask .
docker run -it -p 5000:5000 app-flask
```
After writing the commands on the terminal, your set up is all complete, just open up Docker, run it and click on the "5000:5000", or just type in your browser "localhost:5000" and you are all set up.

## Contributing
Contributions to enhance the functionality, improve performance, or fix any bugs are highly appreciated! Feel free to fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed modifications.

## License
This project is licensed under the UPY university.

## Contact
For any inquiries or feedback, please contact Luis Monterrubio Cota for more information.

Thank you for your interest in the project (SpotFinder)! Happy exploring! 🚀


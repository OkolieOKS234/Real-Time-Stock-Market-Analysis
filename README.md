
# Real-Time Stock Market Analysis

## Overview
This project provides a comprehensive solution for real-time stock market analysis using advanced data processing techniques. It leverages Kafka for data streaming and processing, allowing developers to build scalable and efficient applications.

## Tech Stack + Flow
<ul>
<li>Kafka UI -> Inspect topics/messages</li>
<li>API -> Produces JSON events into Kafka </li>
<li> Spark -> consumes from Kafka, writes to Postgres</li>
<li> Postgres -> stores results for analytics. </li>
<li>pgAdmin -> manage Postgres visually </li>
<li>PowerBI -> external (connects to Postgres database).</li>
</ul>


## Table of Contents
- `[Real-Time Stock Market Analysis](#real-time-stock-market-analysis)`
  - `[Overview](#overview)`
  - `[Tech Stack + Flow](#tech-stack--flow)`
  - `[Table of Contents](#table-of-contents)`
  - `[Installation](#installation)`
  - `[Data Pipeline Architecture](#data-pipeline-architecture)`
  - `[Usage](#usage)`
  - `[Docker Setup](#docker-setup)`
  - `[Contributing](#contributing)`
  - `[License](#license)`

## Installation
To get started with the Real-Time Stock Market Analysis project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/REAL-TIME-STOCK-MARKET-ANALYSIS.git
    cd REAL-TIME-STOCK-MARKET-ANALYSIS
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Data Pipeline Architecture
![Data Pipeline Architecture](./img/real_time_pipeline.png)



## Usage
To run the application, use the following command:
```bash
# Add usage instructions here
docker run --rm confluentinc/cp-kafka:7.4.10 kafka-storage random-uuid

```

## Docker Setup
To set up the Kafka environment using Docker, run the following command:
```bash
docker run --rm confluentinc/cp-kafka:7.4.10 kafka-storage random-uuid
```
This command initializes a Kafka storage with a random UUID, which is essential for the operation of the application.

## Contributing
We welcome contributions to enhance the functionality of this project. Please follow these steps to contribute:

1. `Fork the repository.`
2. `Create a new branch (``git checkout -b feature/YourFeature``)`.
3. `Make your changes and commit them (`git commit -m 'Add some feature'`).`
4. `Push to the branch (``git push origin feature/YourFeature``).`
5. `Open a pull request.`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



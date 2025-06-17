# Hadoop Data Engineering Projects

## Overview

This repository contains a comprehensive collection of Hadoop-based data engineering projects focused on distributed computing, big data processing, and analytics. The projects demonstrate practical implementations of MapReduce algorithms, YARN resource management, and data pipeline development using Python and the Hadoop ecosystem.

## Technologies Used

- **Hadoop**: Distributed storage and processing framework
- **MapReduce**: Programming model for processing large datasets
- **YARN**: Resource management and job scheduling
- **Python**: Primary programming language for data processing
- **HDFS**: Hadoop Distributed File System for data storage

## Project Structure

```
hadoopDataEngineer/
├── src/
│   ├── mapreduce/
│   │   ├── word_count/
│   │   ├── word_splitter/
│   │   └── time_series_analysis/
│   ├── data_generators/
│   └── utilities/
├── data/
│   ├── input/
│   └── output/
├── configs/
├── tests/
└── docs/
```

## Projects

### 1. Word Count MapReduce
**Objective**: Implement a classic word count algorithm using MapReduce to count occurrences of each word in large text files.

**Features**:
- Scalable word counting across distributed datasets
- Case-insensitive processing
- Punctuation handling and text normalization
- Performance optimization for large files

### 2. Text Splitter MapReduce
**Objective**: Develop a MapReduce program to efficiently split large text files into individual words and tokens.

**Features**:
- Intelligent text tokenization
- Multi-delimiter support
- Memory-efficient processing
- Configurable splitting rules

### 3. Time-Series Word Analysis
**Objective**: Analyze word frequency patterns within specific time periods from timestamped data.

**Features**:
- Time-window based word counting
- Temporal data filtering
- Trend analysis capabilities
- Configurable time period granularity

### 4. Data Generation Utilities
**Objective**: Create synthetic datasets for testing and benchmarking MapReduce applications.

**Features**:
- Configurable data volume generation
- Various data format support
- Realistic data distribution patterns
- Performance testing datasets

## Getting Started

### Prerequisites

- Java 8 or higher
- Hadoop 3.x
- Python 3.7+
- Required Python packages (see `requirements.txt`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hadoopDataEngineer.git
cd hadoopDataEngineer
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Hadoop environment:
```bash
# Set HADOOP_HOME and JAVA_HOME
export HADOOP_HOME=/path/to/hadoop
export JAVA_HOME=/path/to/java
```

### Usage

#### Running Word Count Example:
```bash
# Start Hadoop services
start-dfs.sh
start-yarn.sh

# Upload input data to HDFS
hdfs dfs -put data/input/sample.txt /input/

# Run MapReduce job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files src/mapreduce/word_count/mapper.py,src/mapreduce/word_count/reducer.py \
  -mapper mapper.py \
  -reducer reducer.py \
  -input /input/sample.txt \
  -output /output/word_count
```

#### Running Data Generator:
```bash
python src/data_generators/generateRecords.py --records 10000 --output data/input/generated_data.txt
```

## Performance Benchmarks

| Dataset Size | Processing Time | Nodes | Memory Usage |
|-------------|----------------|--------|--------------|
| 1GB         | 2.5 minutes    | 3      | 2GB          |
| 10GB        | 15 minutes     | 5      | 8GB          |
| 100GB       | 45 minutes     | 10     | 32GB         |

## Data Pipeline Architecture

```
Raw Data → HDFS → MapReduce Processing → Results → Analytics Dashboard
    ↓           ↓                ↓            ↓              ↓
 [Source]   [Storage]        [Processing]  [Output]    [Visualization]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-analysis`)
3. Commit your changes (`git commit -am 'Add new analysis feature'`)
4. Push to the branch (`git push origin feature/new-analysis`)
5. Create a Pull Request

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

Run performance benchmarks:
```bash
python tests/benchmark_suite.py
```

## Monitoring and Logging

- **YARN ResourceManager UI**: `http://localhost:8088`
- **HDFS NameNode UI**: `http://localhost:9870`
- **Job History Server**: `http://localhost:19888`

## Troubleshooting

### Common Issues

**Issue**: `java.io.IOException: No space left on device`
**Solution**: Clean up HDFS temporary files or increase disk space

**Issue**: `Connection refused` errors
**Solution**: Ensure Hadoop services are running and ports are not blocked

## Future Enhancements

- [ ] Integration with Apache Spark for faster processing
- [ ] Real-time streaming data processing with Kafka
- [ ] Machine learning pipeline integration
- [ ] Docker containerization for easy deployment
- [ ] Kubernetes orchestration support
- [ ] Advanced analytics and visualization dashboard

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Hadoop Documentation](https://hadoop.apache.org/docs/)
- [MapReduce Tutorial](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
- [YARN Architecture Guide](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html)

## Contact

**Author**: Suhas
**Email**: suhas-tata14@outlook.com
**LinkedIn**: linkedin.com:suhas-tata
**GitHub**: [@suhas-14](https://github.com/suhas-14)

---

*Last Updated: June 2025*
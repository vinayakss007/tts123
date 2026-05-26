# DAaaS Platform - Comprehensive Plan Document
# Data Analytics as a Service

---

## Table of Contents

1. [Executive Summary and Product Vision](#1-executive-summary-and-product-vision)
2. [Core Features and Modules](#2-core-features-and-modules)
3. [AI Integration Architecture](#3-ai-integration-architecture)
4. [Technology Stack Decisions](#4-technology-stack-decisions)
5. [Database Schema Design](#5-database-schema-design)
6. [API Design](#6-api-design)
7. [Frontend Architecture](#7-frontend-architecture)
8. [Authentication and Multi-tenancy](#8-authentication-and-multi-tenancy)
9. [Billing and Subscription Model](#9-billing-and-subscription-model)
10. [Deployment and Infrastructure](#10-deployment-and-infrastructure)
11. [Security Considerations](#11-security-considerations)
12. [Development Phases/Roadmap](#12-development-phasesroadmap)
13. [File/Folder Structure](#13-filefolder-structure)

---

## 1. Executive Summary and Product Vision

### 1.1 Mission Statement

DAaaS (Data Analytics as a Service) empowers small and medium-sized businesses to unlock the full potential of their data without requiring an in-house data science team. By combining AI-powered automation with intuitive user interfaces, we democratize advanced analytics, machine learning, and data visualization for organizations of all sizes.

### 1.2 Problem Statement

SMBs face a critical data gap:

- **Talent scarcity**: Hiring data scientists is expensive (20k-200k+ per year) and competitive
- **Tool complexity**: Existing analytics platforms (Tableau, Power BI, Databricks) require specialized training
- **Time constraints**: Business owners need insights NOW, not after weeks of analysis
- **Fragmented workflows**: Data cleaning, analysis, visualization, and ML require different tools
- **Cost barriers**: Enterprise analytics platforms cost 0k-500k+ annually

The result: 73% of business data goes unanalyzed, leaving revenue and efficiency gains on the table.

### 1.3 Solution Overview

DAaaS provides an all-in-one platform where AI handles the heavy lifting of data analytics:

- **Upload any data source** - CSV, Excel, JSON, database connections, API integrations
- **AI-powered data cleaning** - Automatic detection and resolution of data quality issues
- **One-click visualizations** - AI suggests optimal chart types and generates interactive dashboards
- **Statistical analysis** - From descriptive stats to advanced hypothesis testing, AI-guided
- **ML model generation** - AutoML pipeline that trains, evaluates, and deploys models
- **Natural language reports** - AI generates executive summaries and actionable insights
- **Full user control** - HYBRID approach: AI does all work, users can edit/override everything

### 1.4 Target Audience

| Segment | Size | Pain Point | Key Feature |
|---------|------|------------|-------------|
| Small Business Owners | 1-50 employees | No analytics capability | One-click insights |
| Marketing Teams | 5-200 people | Manual reporting | Automated dashboards |
| Operations Managers | 10-500 people | Spreadsheet overload | Data cleaning + ML |
| E-commerce Companies | Any size | Revenue optimization | Predictive models |
| Financial Services | 10-1000 people | Compliance reporting | Automated reports |
| Healthcare Clinics | 5-200 people | Patient data analysis | Secure analytics |

### 1.5 Value Proposition

- **10x faster**: From raw data to actionable insights in minutes, not weeks
- **90% cost reduction**: Fraction of the cost of hiring a data science team
- **Zero learning curve**: AI handles complexity; users interact in natural language
- **Enterprise-grade security**: SOC 2 compliant, encrypted, tenant-isolated
- **Full transparency**: Every AI decision is explainable and editable

### 1.6 Competitive Advantages

1. **HYBRID AI approach** - Unlike pure-automation tools, users maintain full control
2. **Multi-provider AI** - Not locked into one AI vendor; best model for each task
3. **End-to-end pipeline** - Single platform from data ingestion to ML deployment
4. **Transparent pricing** - Usage-based, no hidden enterprise fees
5. **Self-hostable** - Option for on-premise deployment for sensitive data
6. **API-first** - Every feature accessible programmatically


---

## 2. Core Features and Modules

### 2.1 Data Upload and Ingestion

The data ingestion module is the entry point for all analytics workflows. It supports multiple data sources with automatic schema detection and type inference.

#### Supported Data Sources

| Source Type | Formats/Protocols | Max Size | Features |
|-------------|-------------------|----------|----------|
| File Upload | CSV, Excel (.xlsx/.xls), JSON, Parquet, TSV | 5GB per file | Chunked upload, progress tracking |
| Database Connection | PostgreSQL, MySQL, SQL Server, Oracle, MongoDB | Unlimited | Live sync, scheduled refresh |
| API Integration | REST APIs, GraphQL, Webhooks | Per-request limits | OAuth, API key auth, pagination |
| Cloud Storage | AWS S3, Google Cloud Storage, Azure Blob | Unlimited | Bucket browsing, prefix filtering |
| Streaming | Kafka, Redis Streams, WebSocket feeds | Continuous | Real-time processing, windowing |
| Clipboard/Paste | Raw text, HTML tables | 10MB | Auto-format detection |

#### Upload Pipeline

1. **Chunked Upload** - Large files split into 5MB chunks with resumable uploads
2. **Format Detection** - Automatic identification of file type, encoding, delimiter
3. **Schema Inference** - AI-powered column type detection (numeric, categorical, datetime, text, geo)
4. **Preview Generation** - First 100 rows displayed immediately for user validation
5. **Data Profiling** - Automatic generation of column statistics (nulls, unique values, distributions)
6. **Storage** - Raw data stored in S3, metadata and schema in PostgreSQL, processed data in MongoDB

#### Database Connectors

Each database connector supports:
- Connection pooling for performance
- SSL/TLS encrypted connections
- Read-only access by default (configurable)
- Query builder UI for non-technical users
- Scheduled refresh (hourly, daily, weekly, custom cron)
- Incremental sync for large tables (based on timestamp/ID columns)

### 2.2 Data Cleaning and Preprocessing

AI-powered data cleaning that detects issues and suggests fixes, while allowing users to accept, modify, or reject each suggestion.

#### Cleaning Capabilities

| Issue Type | Detection Method | AI Action | User Override |
|------------|-----------------|-----------|--------------|
| Missing Values | Statistical analysis | Impute (mean/median/mode/AI-predicted) | Choose method or manual value |
| Duplicates | Fuzzy matching + exact | Flag and suggest merge/remove | Select which to keep |
| Outliers | IQR, Z-score, Isolation Forest | Flag and suggest treatment | Keep, remove, or cap |
| Type Mismatches | Pattern recognition | Suggest conversion | Accept or specify format |
| Inconsistent Categories | NLP similarity | Suggest standardization | Map values manually |
| Date Format Issues | Multi-format parser | Auto-convert to ISO 8601 | Specify format |
| Encoding Issues | Charset detection | Auto-fix encoding | Manual encoding selection |
| Whitespace/Formatting | Regex patterns | Trim, normalize | Custom regex rules |

#### Cleaning Workflow

1. **Scan** - AI analyzes entire dataset and produces a Data Quality Report
2. **Prioritize** - Issues ranked by severity (critical/warning/info)
3. **Suggest** - AI generates a fix for each issue with confidence score
4. **Review** - User reviews suggestions in a diff-like interface
5. **Apply** - Accepted changes applied; new dataset version created
6. **Audit** - Complete log of all transformations for reproducibility

#### Preprocessing Pipelines

- **Feature Engineering** - AI suggests new features (ratios, aggregations, time-based features)
- **Normalization** - Min-max scaling, Z-score standardization, log transforms
- **Encoding** - One-hot, label, target, binary encoding for categorical variables
- **Binning** - Equal-width, equal-frequency, custom boundaries
- **Text Processing** - Tokenization, stemming, TF-IDF, embedding generation

### 2.3 Data Visualization

Interactive, AI-suggested visualizations that update in real-time as data changes.

#### Chart Types

| Category | Charts | Use Case |
|----------|--------|----------|
| Comparison | Bar, Grouped Bar, Stacked Bar | Comparing categories |
| Trend | Line, Area, Sparkline | Time series analysis |
| Distribution | Histogram, Box Plot, Violin, Density | Understanding data spread |
| Composition | Pie, Donut, Treemap, Stacked Area | Part-to-whole relationships |
| Relationship | Scatter, Bubble, Heatmap, Correlation Matrix | Variable relationships |
| Geographic | Choropleth, Point Map, Flow Map | Spatial data |
| Statistical | QQ Plot, Residual Plot, Funnel | Statistical analysis |
| Custom | Combination charts, dual-axis | Complex visualizations |

#### AI Visualization Engine

- **Auto-suggestion** - AI analyzes data types and distributions to recommend optimal chart types
- **Smart defaults** - Colors, labels, legends, and formatting chosen automatically
- **Natural language** - Users describe desired visualization in plain English
- **Responsive** - Charts adapt to container size and device type
- **Interactive** - Zoom, pan, hover tooltips, click-to-filter, brush selection
- **Export** - PNG, SVG, PDF, interactive HTML embed

#### Dashboard Builder

- Drag-and-drop layout with grid system
- Real-time data refresh (configurable interval)
- Cross-filtering between charts
- Parameter controls (date pickers, dropdowns, sliders)
- Template library (marketing, finance, operations, executive)
- Sharing with embed codes or public links

### 2.4 Statistical Analysis

From basic descriptive statistics to advanced hypothesis testing, guided by AI.

#### Analysis Types

**Descriptive Statistics:**
- Central tendency (mean, median, mode)
- Dispersion (variance, standard deviation, range, IQR)
- Shape (skewness, kurtosis)
- Frequency tables and distributions

**Inferential Statistics:**
- Confidence intervals
- T-tests (one-sample, two-sample, paired)
- ANOVA (one-way, two-way, repeated measures)
- Chi-square tests (goodness of fit, independence)
- Mann-Whitney U, Kruskal-Wallis (non-parametric)

**Correlation and Regression:**
- Pearson, Spearman, Kendall correlation
- Simple linear regression
- Multiple linear regression
- Logistic regression
- Polynomial regression

**Time Series:**
- Trend decomposition (additive, multiplicative)
- Seasonality detection
- Autocorrelation (ACF, PACF)
- ARIMA/SARIMA modeling
- Exponential smoothing (Holt-Winters)
- Prophet integration for forecasting

**Advanced:**
- Principal Component Analysis (PCA)
- Factor Analysis
- Cluster Analysis (K-means, DBSCAN, hierarchical)
- Survival Analysis (Kaplan-Meier, Cox regression)
- A/B Test Analysis (Bayesian and frequentist)

#### AI-Guided Analysis

- AI suggests appropriate statistical tests based on data characteristics
- Assumption checking automated (normality, homoscedasticity, independence)
- Results explained in plain English with business context
- Effect sizes and practical significance highlighted alongside p-values

### 2.5 ML Model Generation

AutoML pipeline that enables non-technical users to build, evaluate, and deploy machine learning models.

#### Supported Problem Types

| Type | Algorithms | Evaluation Metrics |
|------|-----------|-------------------|
| Classification (Binary) | Logistic Regression, Random Forest, XGBoost, LightGBM, SVM, Neural Net | Accuracy, Precision, Recall, F1, AUC-ROC |
| Classification (Multi-class) | Same as binary + OVR/OVO strategies | Same + Macro/Micro averaging |
| Regression | Linear, Ridge, Lasso, Random Forest, XGBoost, LightGBM, SVR | RMSE, MAE, R-squared, MAPE |
| Clustering | K-Means, DBSCAN, Hierarchical, Gaussian Mixture | Silhouette, Davies-Bouldin, Calinski-Harabasz |
| Time Series Forecasting | ARIMA, Prophet, LSTM, XGBoost (lagged) | RMSE, MAPE, SMAPE |
| Anomaly Detection | Isolation Forest, LOF, Autoencoder | Precision, Recall, F1 |
| NLP | Text Classification, Sentiment, NER | Accuracy, F1, Exact Match |

#### AutoML Pipeline

1. **Problem Definition** - User selects target variable; AI infers problem type
2. **Data Preparation** - Automatic train/test split, cross-validation setup
3. **Feature Selection** - AI ranks features by importance, removes redundant
4. **Algorithm Selection** - Multiple algorithms tried based on data characteristics
5. **Hyperparameter Tuning** - Bayesian optimization (Optuna) for top algorithms
6. **Model Training** - Parallel training of top candidates with progress tracking
7. **Evaluation** - Comprehensive comparison with leaderboard view
8. **Explanation** - SHAP values, feature importance, partial dependence plots
9. **Deployment** - One-click deployment to prediction API endpoint
10. **Monitoring** - Data drift detection, performance degradation alerts

#### Model Management

- Version control for all models
- A/B testing between model versions
- Rollback to previous versions
- Model registry with metadata (accuracy, training date, features used)
- Scheduled retraining on new data

### 2.6 AI-Powered Report Generation

Natural language reports generated from data analysis results.

#### Report Types

- **Executive Summary** - High-level insights for leadership
- **Technical Report** - Detailed methodology and statistical results
- **Trend Analysis** - Changes over time with forecasts
- **Comparative Report** - Before/after, A vs B analysis
- **Anomaly Report** - Unusual patterns and their potential causes
- **Custom Report** - User-defined structure with AI-generated content

#### Report Features

- AI generates insights in natural language
- Charts and tables embedded inline
- Citations linking back to source data
- Confidence levels for each insight
- Recommendations with expected impact
- Export to PDF, Word, HTML, Markdown
- Scheduled generation (daily/weekly/monthly)
- Email delivery to stakeholders
- Template system for consistent branding

### 2.7 Collaboration

Shared workspaces enabling team-based analytics.

#### Collaboration Features

- **Shared Workspaces** - Multiple users in the same organization see the same data
- **Real-time Cursors** - See who is working on what (Google Docs-style)
- **Comments** - Thread-based comments on datasets, charts, and reports
- **Version History** - Every change tracked with rollback capability
- **Permissions** - Granular access control (view, edit, admin) per resource
- **Notifications** - In-app, email, and webhook notifications for changes
- **Activity Feed** - Timeline of all actions in a workspace
- **Sharing** - Public links, embed codes, scheduled email reports


---

## 3. AI Integration Architecture

### 3.1 Single AI Gateway Pattern

All AI interactions flow through a single gateway service that abstracts provider differences and provides a unified interface for the entire platform.

```
+-------------------+     +------------------+     +-------------------+
|   DAaaS Services  | --> |   AI Gateway     | --> |   AI Providers    |
|                   |     |                  |     |                   |
| - Data Cleaning   |     | - Router         |     | - OpenAI (GPT-4)  |
| - Visualization   |     | - Load Balancer  |     | - Anthropic       |
| - Analysis        |     | - Rate Limiter   |     | - Groq (Mixtral)  |
| - ML Generation   |     | - Token Counter  |     | - Ollama (local)  |
| - Report Writer   |     | - Fallback Chain |     | - Any OpenAI-     |
| - NL Interface    |     | - Cache Layer    |     |   compatible API  |
+-------------------+     +------------------+     +-------------------+
```

#### Gateway Responsibilities

1. **Request Routing** - Direct requests to appropriate provider based on task type, model preference, and availability
2. **Protocol Translation** - Convert internal format to provider-specific API formats
3. **Streaming Management** - Handle SSE/WebSocket streaming from providers and forward to clients
4. **Rate Limiting** - Per-user, per-organization, and per-provider rate limiting
5. **Token Accounting** - Count tokens (input + output) and enforce budget limits
6. **Caching** - Semantic cache for identical/similar requests
7. **Fallback** - Automatic failover to backup providers on errors/timeouts
8. **Observability** - Log all requests, latencies, token usage, and errors

### 3.2 Provider Abstraction Layer

Each AI provider is implemented as an adapter conforming to a common interface.

```python
# Provider Interface (Abstract Base Class)
class AIProvider(ABC):
    """Base class for all AI provider adapters."""

    @abstractmethod
    async def complete(self, messages: list[Message], config: CompletionConfig) -> CompletionResponse:
        """Send a completion request and return full response."""
        pass

    @abstractmethod
    async def stream(self, messages: list[Message], config: CompletionConfig) -> AsyncIterator[StreamChunk]:
        """Send a completion request and yield streaming chunks."""
        pass

    @abstractmethod
    async def health_check(self) -> HealthStatus:
        """Check provider availability and latency."""
        pass

    @abstractmethod
    def count_tokens(self, text: str, model: str) -> int:
        """Count tokens for the given text using provider-specific tokenizer."""
        pass

    @abstractmethod
    def get_available_models(self) -> list[ModelInfo]:
        """Return list of available models with capabilities and pricing."""
        pass
```

#### Provider Adapters

| Provider | Adapter Class | Models | Strengths |
|----------|--------------|--------|-----------|
| OpenAI | `OpenAIProvider` | GPT-4o, GPT-4-turbo, GPT-3.5-turbo | Best general reasoning, function calling |
| Anthropic | `AnthropicProvider` | Claude 3.5 Sonnet, Claude 3 Haiku | Long context, nuanced analysis |
| Groq | `GroqProvider` | Mixtral-8x7B, Llama 3 70B | Ultra-fast inference |
| Ollama | `OllamaProvider` | Any GGUF model (Llama, Mistral, etc.) | Local/private, no data leaves server |
| Custom | `OpenAICompatibleProvider` | Any model with OpenAI-compatible API | Self-hosted, custom fine-tuned models |

### 3.3 Model Selection and Switching Logic

The gateway selects the optimal model based on task requirements:

```python
# Model Selection Configuration
MODEL_ROUTING = {
    "data_cleaning": {
        "primary": "gpt-4o",
        "fallback": ["claude-3-5-sonnet", "mixtral-8x7b"],
        "requirements": {"structured_output": True, "max_tokens": 4096}
    },
    "visualization_suggestion": {
        "primary": "gpt-4o",
        "fallback": ["claude-3-5-sonnet"],
        "requirements": {"json_mode": True, "max_tokens": 2048}
    },
    "report_generation": {
        "primary": "claude-3-5-sonnet",
        "fallback": ["gpt-4o", "gpt-4-turbo"],
        "requirements": {"long_context": True, "max_tokens": 8192}
    },
    "quick_analysis": {
        "primary": "groq/mixtral-8x7b",
        "fallback": ["gpt-3.5-turbo", "claude-3-haiku"],
        "requirements": {"low_latency": True, "max_tokens": 2048}
    },
    "ml_code_generation": {
        "primary": "gpt-4o",
        "fallback": ["claude-3-5-sonnet"],
        "requirements": {"code_generation": True, "max_tokens": 4096}
    }
}
```

#### User Model Override

Users can override default model selection at any point:
- Per-organization default model preference
- Per-task model selection dropdown
- Cost-aware selection (show estimated cost per model)
- Quality vs. speed toggle

### 3.4 Streaming Response Handling

Real-time streaming of AI responses using Server-Sent Events (SSE) for HTTP and WebSocket for persistent connections.

```python
# Streaming Architecture
class StreamManager:
    """Manages streaming AI responses to clients."""

    async def stream_to_client(self, request_id: str, provider_stream: AsyncIterator[StreamChunk]):
        """Forward provider stream to client via SSE or WebSocket."""
        buffer = []
        async for chunk in provider_stream:
            # Accumulate for token counting
            buffer.append(chunk)

            # Forward to client immediately
            await self.send_chunk(request_id, {
                "type": "content_delta",
                "content": chunk.text,
                "metadata": {
                    "model": chunk.model,
                    "tokens_so_far": len(buffer),
                    "finish_reason": chunk.finish_reason
                }
            })

        # Final accounting
        total_tokens = sum(c.tokens for c in buffer)
        await self.record_usage(request_id, total_tokens)
```

#### Client-Side Integration

- **SSE endpoint**: `GET /api/v1/ai/stream/{request_id}` - for simple HTTP streaming
- **WebSocket**: `ws://host/ws/ai/` - for bidirectional, persistent streaming
- **Cancellation**: Client can cancel in-progress streams to save tokens
- **Reconnection**: Automatic reconnection with buffer replay on disconnect

### 3.5 Multi-Provider Fallback Chain

Automatic failover ensures high availability of AI capabilities.

```python
# Fallback Configuration
FALLBACK_CONFIG = {
    "max_retries_per_provider": 2,
    "timeout_ms": 30000,
    "health_check_interval_seconds": 30,
    "circuit_breaker": {
        "failure_threshold": 5,      # failures before opening circuit
        "recovery_timeout_seconds": 60,  # time before attempting recovery
        "half_open_requests": 3       # test requests in half-open state
    }
}
```

#### Fallback Logic

1. Try primary provider for the task
2. If timeout/error, retry once with the same provider
3. If still failing, check circuit breaker state
4. Move to next provider in fallback chain
5. If all providers fail, return cached response (if available) or error

#### Health Check System

- Periodic lightweight requests to each provider
- Track latency percentiles (p50, p95, p99)
- Track error rates over sliding window
- Automatic provider removal from rotation if unhealthy
- Alert administrators on provider degradation

### 3.6 Prompt Management System

Centralized prompt management with versioning, A/B testing, and variable injection.

```python
# Prompt Template Example
PROMPT_TEMPLATES = {
    "data_cleaning_suggestions": {
        "version": "2.1.0",
        "template": """You are a data quality expert. Analyze the following dataset sample and identify data quality issues.

Dataset: {{dataset_name}}
Columns: {{column_definitions}}
Sample Rows (first {{sample_size}} rows):
{{sample_data}}

For each issue found, provide:
1. Column affected
2. Issue type (missing, outlier, inconsistent, duplicate, type_mismatch)
3. Severity (critical, warning, info)
4. Suggested fix with confidence score (0-1)
5. SQL/pandas expression to apply the fix

Respond in JSON format.""",
        "variables": ["dataset_name", "column_definitions", "sample_data", "sample_size"],
        "model_preference": "gpt-4o",
        "max_tokens": 4096,
        "temperature": 0.1
    }
}
```

#### Prompt Features

- **Version Control** - All prompts versioned with semantic versioning
- **A/B Testing** - Run multiple prompt versions simultaneously, measure quality
- **Variable Injection** - Dynamic data injection with validation
- **Guardrails** - Output validation schemas, content filtering
- **Analytics** - Track prompt performance (quality scores, token efficiency)
- **Prompt Library** - Reusable prompt components (system instructions, format specs)

### 3.7 Token Usage Tracking and Budget Management

```python
# Token Budget Configuration
TOKEN_BUDGETS = {
    "free": {"monthly_tokens": 50_000, "max_per_request": 2048},
    "starter": {"monthly_tokens": 500_000, "max_per_request": 4096},
    "professional": {"monthly_tokens": 5_000_000, "max_per_request": 8192},
    "enterprise": {"monthly_tokens": None, "max_per_request": 32768}  # unlimited
}
```

#### Tracking System

- Real-time token counting per request (input + output tokens)
- Per-user and per-organization aggregation
- Cost calculation based on provider pricing
- Budget alerts at 50%, 80%, 95% thresholds
- Automatic downgrade to cheaper model at 95% budget
- Hard stop at 100% (unless enterprise with unlimited)
- Historical usage analytics and forecasting

### 3.8 User Edit/Override Workflow

Every AI output follows the HYBRID pattern:

1. **AI Generates** - System produces output (cleaning suggestion, chart, report, model)
2. **User Reviews** - Output presented with explanation and confidence
3. **User Decides** - Accept as-is, modify, or reject
4. **System Learns** - User preferences recorded for future personalization
5. **Audit Trail** - Both AI output and user modifications logged

#### Override Interface Patterns

- **Inline Edit** - Click any AI-generated text/value to modify directly
- **Diff View** - See what AI changed vs. original data
- **Batch Accept/Reject** - For cleaning suggestions, accept/reject in bulk
- **Preference Memory** - System remembers choices (e.g., "always use median for missing numerics")
- **Undo/Redo** - Full undo history for all AI actions


---

## 4. Technology Stack Decisions

### 4.1 Backend: Django 5.x + Django REST Framework

**Choice Justification:**

| Factor | Django + DRF | Alternatives Considered |
|--------|-------------|------------------------|
| Maturity | 18+ years, battle-tested | FastAPI (newer, less ecosystem) |
| ORM | Powerful built-in ORM with migrations | SQLAlchemy (more verbose) |
| Admin | Auto-generated admin panel | Manual admin for others |
| Security | Built-in CSRF, XSS, SQL injection protection | Manual implementation |
| Ecosystem | 5000+ packages on PyPI | Smaller ecosystems |
| Async | Full async support since Django 4.1 | Native in FastAPI |
| ML Integration | Python ecosystem (scikit-learn, pandas) | Language barrier with Go/Node |

**Key Django Configuration:**
- Django 5.x with async views and ORM
- Django REST Framework for API layer
- Django Channels for WebSocket support
- Django Celery Beat for scheduled tasks
- Django Filter for query filtering
- Django CORS Headers for frontend integration
- drf-spectacular for OpenAPI schema generation

### 4.2 Frontend: React 18 + TypeScript + Vite

**Choice Justification:**

| Factor | React + TypeScript | Alternatives Considered |
|--------|-------------------|------------------------|
| Ecosystem | Largest component ecosystem | Vue (smaller), Angular (opinionated) |
| Type Safety | Full TypeScript support | PropTypes (weaker) |
| Performance | Concurrent rendering, Suspense | Similar across modern frameworks |
| Hiring | Largest developer pool | Smaller pools for others |
| Charting | Plotly, D3, Recharts all have React bindings | Good in Vue/Angular too |
| Build Tool | Vite (fast HMR, ESM-native) | Webpack (slower), Turbopack (immature) |

**Frontend Libraries:**
- React 18 with Concurrent Features
- TypeScript 5.x (strict mode)
- Vite 5.x for development and builds
- React Router v6 for routing
- Zustand for state management (lightweight, TypeScript-first)
- TanStack Query (React Query) for server state
- Tailwind CSS 3.x + shadcn/ui for styling and components
- Plotly.js for interactive charts
- D3.js for custom visualizations
- React Hook Form + Zod for form validation
- Axios for HTTP client

### 4.3 Databases: PostgreSQL 16 + MongoDB 7

**Dual Database Strategy:**

| Data Type | Database | Justification |
|-----------|----------|---------------|
| Users, Orgs, Auth | PostgreSQL | Relational, ACID, joins |
| Billing, Subscriptions | PostgreSQL | Transactional integrity |
| ML Models metadata | PostgreSQL | Complex queries, foreign keys |
| Dataset metadata | PostgreSQL | Schema enforcement |
| Raw uploaded data | MongoDB | Schema-flexible, large documents |
| Dataset rows | MongoDB | Variable columns per dataset |
| AI conversation history | MongoDB | Nested, variable structure |
| Analysis results | MongoDB | Complex nested JSON |
| Audit logs | MongoDB | High-write, append-only |

**PostgreSQL Configuration:**
- Version 16 with parallel query and improved JSON support
- Row-level security for tenant isolation
- Partitioning for large tables (audit_logs, usage_records)
- Full-text search (tsvector) for dataset/report search
- pgvector extension for AI embedding storage

**MongoDB Configuration:**
- Version 7 with native time series collections
- WiredTiger storage engine
- Sharding for large datasets
- TTL indexes for temporary data
- Change streams for real-time updates

### 4.4 Cache/Queue: Redis 7 + Celery 5

**Redis Usage:**
- Session storage (JWT blacklist)
- API response caching
- Rate limiting counters
- Real-time pub/sub for WebSocket messages
- Celery message broker
- AI response caching (semantic cache)
- Feature flags storage

**Celery Configuration:**
- Task queues: default, priority, ml_training, data_processing, reports
- Concurrency: prefork for CPU tasks, gevent for I/O tasks
- Task routing based on resource requirements
- Dead letter queue for failed tasks
- Task result backend (Redis)
- Periodic tasks via Celery Beat (scheduled reports, health checks, cleanup)

### 4.5 Storage: S3-Compatible (AWS S3 / MinIO)

| Storage Use Case | Bucket | Lifecycle |
|-----------------|--------|-----------|
| Raw uploaded files | `daaas-uploads-raw` | 90 days after processing |
| Processed datasets | `daaas-datasets` | Per retention policy |
| Generated reports (PDF) | `daaas-reports` | Indefinite |
| ML model artifacts | `daaas-models` | Versioned, indefinite |
| Chart images (exports) | `daaas-exports` | 30 days |
| Temporary files | `daaas-temp` | 24 hours |

**Local Development:** MinIO (S3-compatible, Docker container)
**Production:** AWS S3 with intelligent tiering

### 4.6 Real-time: Django Channels + WebSockets

**WebSocket Use Cases:**
- AI streaming responses (token by token)
- Real-time collaboration (cursors, edits)
- Live dashboard updates
- ML training progress
- Data processing progress
- Notification delivery

**Channel Layer:** Redis-backed with automatic reconnection and message buffering.

### 4.7 ML Libraries

| Library | Use Case | Version |
|---------|----------|---------|
| scikit-learn | Classical ML algorithms, preprocessing | 1.4+ |
| XGBoost | Gradient boosting (tabular data champion) | 2.0+ |
| LightGBM | Fast gradient boosting, large datasets | 4.0+ |
| PyTorch | Optional deep learning, embeddings | 2.0+ |
| Optuna | Hyperparameter optimization | 3.5+ |
| SHAP | Model explainability | 0.44+ |
| pandas | Data manipulation and analysis | 2.1+ |
| numpy | Numerical computing | 1.26+ |
| scipy | Statistical functions | 1.12+ |
| statsmodels | Statistical modeling | 0.14+ |
| Prophet | Time series forecasting | 1.1+ |

### 4.8 Visualization Libraries

**Backend (chart generation for reports/exports):**
- Matplotlib + Seaborn for static chart generation
- Plotly for server-side interactive HTML generation

**Frontend (interactive dashboards):**
- Plotly.js for standard interactive charts
- D3.js for custom/complex visualizations
- React-Plotly.js for React integration

### 4.9 Containerization and Orchestration

**Development:** Docker Compose with hot-reload
- Backend (Django) with volume mounts
- Frontend (Vite dev server) with HMR
- PostgreSQL 16
- MongoDB 7
- Redis 7
- MinIO (S3)
- Celery workers
- Flower (Celery monitoring)

**Production:** Kubernetes (EKS/AKS/GKE)
- Horizontal Pod Autoscaler for web workers
- Separate node pools for ML workloads (GPU-capable)
- Istio service mesh for internal communication
- Cert-manager for TLS certificates
- External-DNS for automatic DNS management

### 4.10 CI/CD: GitHub Actions

**Pipeline Stages:**
1. Lint and format check (ruff, black, eslint, prettier)
2. Unit tests (pytest, jest)
3. Integration tests (Docker Compose)
4. Security scanning (Snyk, Trivy)
5. Build Docker images
6. Push to container registry
7. Deploy to staging (automatic)
8. E2E tests against staging
9. Deploy to production (manual approval)

### 4.11 Monitoring: Prometheus + Grafana + Sentry

| Tool | Purpose |
|------|---------|
| Prometheus | Metrics collection (CPU, memory, request rates, latencies) |
| Grafana | Dashboards and visualization of metrics |
| Sentry | Error tracking and performance monitoring |
| Loki | Log aggregation and search |
| Jaeger | Distributed tracing |
| PagerDuty | Alerting and incident management |


---

## 5. Database Schema Design

### 5.1 PostgreSQL Schema

#### Users and Authentication

```sql
-- Organizations (tenants)
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    logo_url TEXT,
    settings JSONB DEFAULT '{}',
    subscription_plan VARCHAR(50) DEFAULT 'free',
    stripe_customer_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_organizations_slug ON organizations(slug);
CREATE INDEX idx_organizations_stripe ON organizations(stripe_customer_id);

-- Users
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    avatar_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    is_email_verified BOOLEAN DEFAULT FALSE,
    last_login_at TIMESTAMP WITH TIME ZONE,
    settings JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);

-- Organization Memberships (M2M with roles)
CREATE TABLE memberships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL CHECK (role IN ('owner', 'admin', 'analyst', 'viewer')),
    invited_by UUID REFERENCES users(id),
    accepted_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(user_id, organization_id)
);

CREATE INDEX idx_memberships_user ON memberships(user_id);
CREATE INDEX idx_memberships_org ON memberships(organization_id);
CREATE INDEX idx_memberships_role ON memberships(organization_id, role);

-- OAuth Connections
CREATE TABLE oauth_connections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    provider VARCHAR(50) NOT NULL,  -- 'google', 'github', 'microsoft'
    provider_user_id VARCHAR(255) NOT NULL,
    access_token TEXT,
    refresh_token TEXT,
    token_expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(provider, provider_user_id)
);

-- API Keys
CREATE TABLE api_keys (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    key_hash VARCHAR(255) NOT NULL,
    key_prefix VARCHAR(10) NOT NULL,  -- first 8 chars for identification
    scopes JSONB DEFAULT '["read"]',
    last_used_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_api_keys_hash ON api_keys(key_hash);
CREATE INDEX idx_api_keys_org ON api_keys(organization_id);
```

#### Datasets and Data Management

```sql
-- Datasets
CREATE TABLE datasets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    source_type VARCHAR(50) NOT NULL,  -- 'upload', 'database', 'api', 'streaming'
    source_config JSONB,  -- connection details (encrypted fields)
    status VARCHAR(30) DEFAULT 'pending',  -- pending, processing, ready, error
    row_count BIGINT DEFAULT 0,
    column_count INTEGER DEFAULT 0,
    file_size_bytes BIGINT DEFAULT 0,
    storage_path TEXT,  -- S3 path for raw file
    tags TEXT[] DEFAULT '{}',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_datasets_org ON datasets(organization_id);
CREATE INDEX idx_datasets_status ON datasets(organization_id, status);
CREATE INDEX idx_datasets_tags ON datasets USING GIN(tags);
CREATE INDEX idx_datasets_search ON datasets USING GIN(to_tsvector('english', name || ' ' || COALESCE(description, '')));

-- Dataset Versions (immutable snapshots)
CREATE TABLE dataset_versions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    dataset_id UUID NOT NULL REFERENCES datasets(id) ON DELETE CASCADE,
    version_number INTEGER NOT NULL,
    created_by UUID NOT NULL REFERENCES users(id),
    change_description TEXT,
    row_count BIGINT NOT NULL,
    storage_path TEXT NOT NULL,  -- S3 path for this version
    schema_snapshot JSONB NOT NULL,  -- column definitions at this version
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(dataset_id, version_number)
);

CREATE INDEX idx_dataset_versions_dataset ON dataset_versions(dataset_id);

-- Data Columns (schema definition)
CREATE TABLE data_columns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    dataset_id UUID NOT NULL REFERENCES datasets(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    display_name VARCHAR(255),
    data_type VARCHAR(50) NOT NULL,  -- 'integer', 'float', 'string', 'datetime', 'boolean', 'json'
    nullable BOOLEAN DEFAULT TRUE,
    position INTEGER NOT NULL,
    statistics JSONB,  -- min, max, mean, nulls, unique count, distribution
    ai_inferred_type VARCHAR(50),  -- AI's best guess at semantic type
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(dataset_id, name)
);

CREATE INDEX idx_data_columns_dataset ON data_columns(dataset_id);

-- Data Connections (for live database/API sources)
CREATE TABLE data_connections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    connection_type VARCHAR(50) NOT NULL,  -- 'postgresql', 'mysql', 'mongodb', 'rest_api'
    config_encrypted TEXT NOT NULL,  -- encrypted connection string/config
    is_active BOOLEAN DEFAULT TRUE,
    last_sync_at TIMESTAMP WITH TIME ZONE,
    sync_schedule VARCHAR(100),  -- cron expression
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_data_connections_org ON data_connections(organization_id);
```

#### Analysis and Visualization

```sql
-- Analysis Sessions
CREATE TABLE analysis_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    dataset_id UUID NOT NULL REFERENCES datasets(id),
    created_by UUID NOT NULL REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    session_type VARCHAR(50) NOT NULL,  -- 'exploratory', 'statistical', 'ml', 'report'
    status VARCHAR(30) DEFAULT 'active',  -- active, completed, archived
    config JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_analysis_sessions_org ON analysis_sessions(organization_id);
CREATE INDEX idx_analysis_sessions_dataset ON analysis_sessions(dataset_id);

-- Analysis Steps (individual operations within a session)
CREATE TABLE analysis_steps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES analysis_sessions(id) ON DELETE CASCADE,
    step_number INTEGER NOT NULL,
    step_type VARCHAR(50) NOT NULL,  -- 'clean', 'transform', 'visualize', 'stat_test', 'ml_train'
    input_config JSONB NOT NULL,  -- parameters for this step
    output_result JSONB,  -- results/output of this step
    ai_suggestion JSONB,  -- what AI suggested
    user_override JSONB,  -- what user changed (if anything)
    status VARCHAR(30) DEFAULT 'pending',  -- pending, running, completed, error
    execution_time_ms INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_analysis_steps_session ON analysis_steps(session_id);

-- Visualizations
CREATE TABLE visualizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    dataset_id UUID NOT NULL REFERENCES datasets(id),
    created_by UUID NOT NULL REFERENCES users(id),
    session_id UUID REFERENCES analysis_sessions(id),
    name VARCHAR(255) NOT NULL,
    chart_type VARCHAR(50) NOT NULL,  -- 'bar', 'line', 'scatter', 'pie', 'heatmap', etc.
    config JSONB NOT NULL,  -- chart configuration (axes, colors, filters)
    data_query JSONB,  -- query to fetch chart data
    thumbnail_url TEXT,  -- pre-rendered thumbnail
    is_pinned BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_visualizations_org ON visualizations(organization_id);
CREATE INDEX idx_visualizations_dataset ON visualizations(dataset_id);

-- Dashboards
CREATE TABLE dashboards (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    layout JSONB NOT NULL DEFAULT '[]',  -- grid layout configuration
    is_public BOOLEAN DEFAULT FALSE,
    public_slug VARCHAR(100) UNIQUE,
    refresh_interval_seconds INTEGER DEFAULT 0,  -- 0 = manual refresh
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_dashboards_org ON dashboards(organization_id);
CREATE INDEX idx_dashboards_public ON dashboards(public_slug) WHERE is_public = TRUE;

-- Dashboard Widgets (M2M between dashboards and visualizations)
CREATE TABLE dashboard_widgets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    dashboard_id UUID NOT NULL REFERENCES dashboards(id) ON DELETE CASCADE,
    visualization_id UUID REFERENCES visualizations(id) ON DELETE SET NULL,
    widget_type VARCHAR(50) NOT NULL,  -- 'chart', 'metric', 'table', 'text'
    position_x INTEGER NOT NULL,
    position_y INTEGER NOT NULL,
    width INTEGER NOT NULL DEFAULT 6,
    height INTEGER NOT NULL DEFAULT 4,
    config JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_dashboard_widgets_dashboard ON dashboard_widgets(dashboard_id);
```

#### ML Models

```sql
-- ML Models
CREATE TABLE ml_models (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    dataset_id UUID NOT NULL REFERENCES datasets(id),
    created_by UUID NOT NULL REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    problem_type VARCHAR(50) NOT NULL,  -- 'classification', 'regression', 'clustering', 'forecasting'
    target_column VARCHAR(255),
    feature_columns JSONB NOT NULL DEFAULT '[]',
    status VARCHAR(30) DEFAULT 'draft',  -- draft, training, trained, deployed, retired
    best_algorithm VARCHAR(100),
    best_metrics JSONB,  -- {accuracy: 0.95, f1: 0.93, ...}
    deployment_endpoint TEXT,  -- API endpoint for predictions
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_ml_models_org ON ml_models(organization_id);
CREATE INDEX idx_ml_models_status ON ml_models(organization_id, status);

-- Training Runs
CREATE TABLE training_runs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    model_id UUID NOT NULL REFERENCES ml_models(id) ON DELETE CASCADE,
    algorithm VARCHAR(100) NOT NULL,  -- 'random_forest', 'xgboost', 'lightgbm', etc.
    hyperparameters JSONB NOT NULL,
    metrics JSONB NOT NULL,  -- evaluation metrics
    training_duration_seconds INTEGER,
    dataset_version_id UUID REFERENCES dataset_versions(id),
    artifact_path TEXT,  -- S3 path to serialized model
    feature_importance JSONB,
    confusion_matrix JSONB,
    status VARCHAR(30) DEFAULT 'pending',  -- pending, running, completed, failed
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_training_runs_model ON training_runs(model_id);
CREATE INDEX idx_training_runs_status ON training_runs(model_id, status);

-- Model Versions (deployed versions)
CREATE TABLE model_versions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    model_id UUID NOT NULL REFERENCES ml_models(id) ON DELETE CASCADE,
    training_run_id UUID NOT NULL REFERENCES training_runs(id),
    version_number INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,  -- currently serving predictions
    deployment_config JSONB,
    serving_stats JSONB DEFAULT '{}',  -- request count, avg latency, etc.
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(model_id, version_number)
);

CREATE INDEX idx_model_versions_active ON model_versions(model_id) WHERE is_active = TRUE;

-- Predictions (logged for monitoring)
CREATE TABLE predictions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    model_version_id UUID NOT NULL REFERENCES model_versions(id),
    input_data JSONB NOT NULL,
    prediction_result JSONB NOT NULL,
    confidence FLOAT,
    latency_ms INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
) PARTITION BY RANGE (created_at);

-- Create monthly partitions
CREATE TABLE predictions_current PARTITION OF predictions
    FOR VALUES FROM (CURRENT_DATE) TO (CURRENT_DATE + INTERVAL '1 month');
```

#### Reports

```sql
-- Reports
CREATE TABLE reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id),
    dataset_id UUID REFERENCES datasets(id),
    session_id UUID REFERENCES analysis_sessions(id),
    name VARCHAR(255) NOT NULL,
    report_type VARCHAR(50) NOT NULL,  -- 'executive', 'technical', 'trend', 'comparative', 'custom'
    status VARCHAR(30) DEFAULT 'draft',  -- draft, generating, completed, error
    content_markdown TEXT,  -- generated markdown content
    content_html TEXT,  -- rendered HTML
    pdf_url TEXT,  -- exported PDF path
    schedule VARCHAR(100),  -- cron expression for recurring reports
    recipients JSONB DEFAULT '[]',  -- email recipients for scheduled reports
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_reports_org ON reports(organization_id);

-- Report Sections
CREATE TABLE report_sections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id UUID NOT NULL REFERENCES reports(id) ON DELETE CASCADE,
    section_number INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    content_markdown TEXT NOT NULL,
    ai_generated BOOLEAN DEFAULT TRUE,
    user_edited BOOLEAN DEFAULT FALSE,
    visualization_ids UUID[] DEFAULT '{}',  -- linked charts
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_report_sections_report ON report_sections(report_id);

-- AI Generations (log all AI outputs)
CREATE TABLE ai_generations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id),
    generation_type VARCHAR(50) NOT NULL,  -- 'cleaning', 'visualization', 'report', 'analysis', 'code'
    provider VARCHAR(50) NOT NULL,  -- 'openai', 'anthropic', 'groq', 'ollama'
    model VARCHAR(100) NOT NULL,  -- 'gpt-4o', 'claude-3-5-sonnet', etc.
    prompt_template VARCHAR(100),  -- reference to prompt template used
    input_tokens INTEGER NOT NULL,
    output_tokens INTEGER NOT NULL,
    total_cost_cents INTEGER DEFAULT 0,
    latency_ms INTEGER,
    status VARCHAR(30) NOT NULL,  -- 'success', 'error', 'timeout', 'cancelled'
    user_accepted BOOLEAN,  -- did user accept the AI output?
    user_modified BOOLEAN,  -- did user modify the AI output?
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
) PARTITION BY RANGE (created_at);

CREATE INDEX idx_ai_generations_org ON ai_generations(organization_id);
CREATE INDEX idx_ai_generations_type ON ai_generations(generation_type);
```

#### Billing and Subscriptions

```sql
-- Subscription Plans (static reference)
CREATE TABLE plans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL UNIQUE,  -- 'free', 'starter', 'professional', 'enterprise'
    display_name VARCHAR(100) NOT NULL,
    price_monthly_cents INTEGER NOT NULL,
    price_yearly_cents INTEGER NOT NULL,
    stripe_price_id_monthly VARCHAR(255),
    stripe_price_id_yearly VARCHAR(255),
    limits JSONB NOT NULL,  -- {datasets: 5, storage_gb: 1, ai_tokens: 50000, ...}
    features JSONB NOT NULL,  -- {collaboration: true, api_access: false, ...}
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Subscriptions
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    plan_id UUID NOT NULL REFERENCES plans(id),
    stripe_subscription_id VARCHAR(255),
    status VARCHAR(30) NOT NULL,  -- 'active', 'past_due', 'cancelled', 'trialing'
    billing_cycle VARCHAR(20) NOT NULL,  -- 'monthly', 'yearly'
    current_period_start TIMESTAMP WITH TIME ZONE NOT NULL,
    current_period_end TIMESTAMP WITH TIME ZONE NOT NULL,
    cancel_at_period_end BOOLEAN DEFAULT FALSE,
    trial_ends_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_subscriptions_org ON subscriptions(organization_id);
CREATE INDEX idx_subscriptions_stripe ON subscriptions(stripe_subscription_id);

-- Usage Records (metering)
CREATE TABLE usage_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    metric_type VARCHAR(50) NOT NULL,  -- 'ai_tokens', 'storage_bytes', 'compute_seconds', 'api_calls'
    quantity BIGINT NOT NULL,
    unit_cost_cents INTEGER DEFAULT 0,
    period_start TIMESTAMP WITH TIME ZONE NOT NULL,
    period_end TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
) PARTITION BY RANGE (created_at);

CREATE INDEX idx_usage_records_org ON usage_records(organization_id);
CREATE INDEX idx_usage_records_metric ON usage_records(organization_id, metric_type);

-- Invoices
CREATE TABLE invoices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    stripe_invoice_id VARCHAR(255),
    amount_cents INTEGER NOT NULL,
    currency VARCHAR(3) DEFAULT 'usd',
    status VARCHAR(30) NOT NULL,  -- 'draft', 'open', 'paid', 'void', 'uncollectible'
    line_items JSONB NOT NULL DEFAULT '[]',
    pdf_url TEXT,
    period_start TIMESTAMP WITH TIME ZONE NOT NULL,
    period_end TIMESTAMP WITH TIME ZONE NOT NULL,
    paid_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_invoices_org ON invoices(organization_id);
CREATE INDEX idx_invoices_status ON invoices(organization_id, status);
```

#### System Tables

```sql
-- Audit Logs
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id),
    action VARCHAR(100) NOT NULL,  -- 'dataset.create', 'model.deploy', 'user.invite', etc.
    resource_type VARCHAR(50) NOT NULL,
    resource_id UUID,
    changes JSONB,  -- {field: {old: x, new: y}}
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
) PARTITION BY RANGE (created_at);

CREATE INDEX idx_audit_logs_org ON audit_logs(organization_id);
CREATE INDEX idx_audit_logs_user ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_action ON audit_logs(action);
CREATE INDEX idx_audit_logs_resource ON audit_logs(resource_type, resource_id);

-- Notifications
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL,  -- 'info', 'warning', 'success', 'error'
    category VARCHAR(50) NOT NULL,  -- 'system', 'collaboration', 'ml', 'billing'
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    action_url TEXT,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_notifications_user ON notifications(user_id, is_read);
CREATE INDEX idx_notifications_org ON notifications(organization_id);
```

### 5.2 MongoDB Collections

```javascript
// Dataset Rows (actual data stored per dataset)
// Collection: dataset_rows_{dataset_id}
{
    "_id": ObjectId,
    "dataset_id": UUID,
    "version": Integer,
    "row_index": Integer,
    "data": {
        "column_name_1": "value",
        "column_name_2": 123.45,
        "column_name_3": ISODate("2024-01-15"),
        // ... dynamic columns based on dataset schema
    },
    "metadata": {
        "imported_at": ISODate,
        "source_row": Integer,
        "quality_flags": ["missing_value", "outlier"]
    }
}
// Indexes: {dataset_id: 1, version: 1, row_index: 1}

// AI Conversation History
// Collection: ai_conversations
{
    "_id": ObjectId,
    "organization_id": UUID,
    "user_id": UUID,
    "session_id": UUID,
    "messages": [
        {
            "role": "user",
            "content": "Show me the trend of sales over time",
            "timestamp": ISODate
        },
        {
            "role": "assistant",
            "content": "Based on your data, here is the sales trend...",
            "metadata": {
                "model": "gpt-4o",
                "tokens": 450,
                "latency_ms": 1200
            },
            "timestamp": ISODate
        }
    ],
    "context": {
        "dataset_id": UUID,
        "active_filters": {},
        "selected_columns": []
    },
    "created_at": ISODate,
    "updated_at": ISODate
}
// Indexes: {organization_id: 1, user_id: 1, created_at: -1}

// Analysis Results Cache
// Collection: analysis_results
{
    "_id": ObjectId,
    "session_id": UUID,
    "step_id": UUID,
    "result_type": "statistical_test",
    "result_data": {
        "test_name": "two_sample_t_test",
        "statistic": 2.45,
        "p_value": 0.014,
        "confidence_interval": [0.12, 0.89],
        "effect_size": 0.34,
        "interpretation": "Statistically significant difference..."
    },
    "computed_at": ISODate,
    "ttl": ISODate  // auto-expire after 30 days
}
// Indexes: {session_id: 1, step_id: 1}, TTL index on ttl field
```


---

## 6. API Design

### 6.1 API Conventions

- **Base URL**: `https://api.daaas.io/api/v1/`
- **Versioning**: URL prefix (`/api/v1/`, `/api/v2/`)
- **Format**: JSON (request and response bodies)
- **Authentication**: Bearer token (JWT) or API key in header
- **Pagination**: Cursor-based for lists (default 20, max 100 items)
- **Filtering**: Query parameters with field lookups (`?status=active&created_after=2024-01-01`)
- **Sorting**: `?ordering=-created_at,name`
- **Error Format**: RFC 7807 Problem Details

```json
{
    "type": "https://api.daaas.io/errors/validation",
    "title": "Validation Error",
    "status": 422,
    "detail": "The provided data failed validation checks.",
    "errors": [
        {"field": "email", "message": "A valid email address is required."}
    ]
}
```

### 6.2 Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register new user + organization |
| POST | `/api/v1/auth/login` | Login with email/password |
| POST | `/api/v1/auth/refresh` | Refresh JWT token |
| POST | `/api/v1/auth/logout` | Invalidate refresh token |
| POST | `/api/v1/auth/forgot-password` | Send password reset email |
| POST | `/api/v1/auth/reset-password` | Reset password with token |
| POST | `/api/v1/auth/verify-email` | Verify email address |
| GET | `/api/v1/auth/oauth/{provider}/authorize` | Initiate OAuth flow |
| POST | `/api/v1/auth/oauth/{provider}/callback` | OAuth callback |
| GET | `/api/v1/auth/me` | Get current user profile |
| PATCH | `/api/v1/auth/me` | Update profile |

**Login Request/Response Example:**

```json
// POST /api/v1/auth/login
// Request
{
    "email": "user@company.com",
    "password": "securepassword123"
}

// Response (200 OK)
{
    "access_token": "eyJhbGciOiJSUzI1NiIs...",
    "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2...",
    "token_type": "Bearer",
    "expires_in": 900,
    "user": {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "email": "user@company.com",
        "first_name": "John",
        "last_name": "Doe",
        "organizations": [
            {"id": "...", "name": "Acme Corp", "role": "admin"}
        ]
    }
}
```

### 6.3 Organization Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/organizations` | List user's organizations |
| POST | `/api/v1/organizations` | Create new organization |
| GET | `/api/v1/organizations/{org_id}` | Get organization details |
| PATCH | `/api/v1/organizations/{org_id}` | Update organization |
| DELETE | `/api/v1/organizations/{org_id}` | Delete organization |
| GET | `/api/v1/organizations/{org_id}/members` | List members |
| POST | `/api/v1/organizations/{org_id}/members/invite` | Invite member |
| PATCH | `/api/v1/organizations/{org_id}/members/{user_id}` | Update member role |
| DELETE | `/api/v1/organizations/{org_id}/members/{user_id}` | Remove member |

### 6.4 Dataset Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/datasets` | List datasets |
| POST | `/api/v1/datasets` | Create dataset metadata |
| GET | `/api/v1/datasets/{id}` | Get dataset details |
| PATCH | `/api/v1/datasets/{id}` | Update dataset metadata |
| DELETE | `/api/v1/datasets/{id}` | Delete dataset |
| POST | `/api/v1/datasets/{id}/upload` | Upload file data (multipart) |
| POST | `/api/v1/datasets/{id}/upload/chunk` | Upload chunk (resumable) |
| GET | `/api/v1/datasets/{id}/preview` | Get first N rows |
| GET | `/api/v1/datasets/{id}/columns` | Get column definitions |
| GET | `/api/v1/datasets/{id}/statistics` | Get column statistics |
| GET | `/api/v1/datasets/{id}/versions` | List versions |
| POST | `/api/v1/datasets/{id}/versions` | Create new version |
| GET | `/api/v1/datasets/{id}/quality-report` | Get data quality report |
| POST | `/api/v1/datasets/{id}/clean` | Apply cleaning operations |
| POST | `/api/v1/datasets/{id}/connect` | Connect external data source |
| POST | `/api/v1/datasets/{id}/sync` | Trigger sync from source |

**Upload Request Example:**

```json
// POST /api/v1/datasets/{id}/upload
// Content-Type: multipart/form-data
// Body: file=@data.csv

// Response (202 Accepted)
{
    "id": "dataset-uuid",
    "status": "processing",
    "upload_id": "upload-uuid",
    "progress_url": "/api/v1/datasets/{id}/upload/status/{upload_id}"
}
```

### 6.5 Analytics Session Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/sessions` | List analysis sessions |
| POST | `/api/v1/sessions` | Create new session |
| GET | `/api/v1/sessions/{id}` | Get session details + steps |
| PATCH | `/api/v1/sessions/{id}` | Update session |
| DELETE | `/api/v1/sessions/{id}` | Delete session |
| GET | `/api/v1/sessions/{id}/steps` | List steps |
| POST | `/api/v1/sessions/{id}/steps` | Add analysis step |
| POST | `/api/v1/sessions/{id}/steps/{step_id}/execute` | Execute step |
| POST | `/api/v1/sessions/{id}/steps/{step_id}/override` | Override AI suggestion |

### 6.6 Visualization Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/visualizations` | List visualizations |
| POST | `/api/v1/visualizations` | Create visualization |
| GET | `/api/v1/visualizations/{id}` | Get visualization config + data |
| PATCH | `/api/v1/visualizations/{id}` | Update visualization |
| DELETE | `/api/v1/visualizations/{id}` | Delete visualization |
| POST | `/api/v1/visualizations/suggest` | AI suggests chart for data |
| POST | `/api/v1/visualizations/{id}/export` | Export as PNG/SVG/PDF |
| GET | `/api/v1/dashboards` | List dashboards |
| POST | `/api/v1/dashboards` | Create dashboard |
| GET | `/api/v1/dashboards/{id}` | Get dashboard with widgets |
| PATCH | `/api/v1/dashboards/{id}` | Update dashboard layout |
| DELETE | `/api/v1/dashboards/{id}` | Delete dashboard |
| POST | `/api/v1/dashboards/{id}/widgets` | Add widget |
| PATCH | `/api/v1/dashboards/{id}/widgets/{widget_id}` | Update widget |
| DELETE | `/api/v1/dashboards/{id}/widgets/{widget_id}` | Remove widget |

### 6.7 ML Model Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/models` | List ML models |
| POST | `/api/v1/models` | Create model definition |
| GET | `/api/v1/models/{id}` | Get model details |
| PATCH | `/api/v1/models/{id}` | Update model config |
| DELETE | `/api/v1/models/{id}` | Delete model |
| POST | `/api/v1/models/{id}/train` | Start training run |
| GET | `/api/v1/models/{id}/training-runs` | List training runs |
| GET | `/api/v1/models/{id}/training-runs/{run_id}` | Get run details |
| POST | `/api/v1/models/{id}/deploy` | Deploy model version |
| POST | `/api/v1/models/{id}/predict` | Make prediction |
| POST | `/api/v1/models/{id}/batch-predict` | Batch predictions |
| GET | `/api/v1/models/{id}/versions` | List model versions |
| GET | `/api/v1/models/{id}/explain` | Get model explainability |
| GET | `/api/v1/models/{id}/metrics` | Get serving metrics |

**Prediction Request/Response:**

```json
// POST /api/v1/models/{id}/predict
// Request
{
    "features": {
        "age": 35,
        "income": 75000,
        "location": "urban",
        "purchase_history": 12
    }
}

// Response (200 OK)
{
    "prediction": "high_value",
    "confidence": 0.87,
    "probabilities": {
        "high_value": 0.87,
        "medium_value": 0.10,
        "low_value": 0.03
    },
    "explanation": {
        "top_features": [
            {"feature": "income", "contribution": 0.45},
            {"feature": "purchase_history", "contribution": 0.32}
        ]
    },
    "model_version": "v3",
    "latency_ms": 12
}
```

### 6.8 Report Generation Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/reports` | List reports |
| POST | `/api/v1/reports` | Create/generate report |
| GET | `/api/v1/reports/{id}` | Get report content |
| PATCH | `/api/v1/reports/{id}` | Update report (user edits) |
| DELETE | `/api/v1/reports/{id}` | Delete report |
| POST | `/api/v1/reports/{id}/regenerate` | Regenerate with AI |
| POST | `/api/v1/reports/{id}/export` | Export (PDF/Word/HTML) |
| GET | `/api/v1/reports/{id}/sections` | List sections |
| PATCH | `/api/v1/reports/{id}/sections/{section_id}` | Edit section |
| POST | `/api/v1/reports/{id}/schedule` | Set up recurring generation |

### 6.9 AI Gateway Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/ai/completions` | Standard AI completion |
| POST | `/api/v1/ai/completions/stream` | Streaming AI completion |
| GET | `/api/v1/ai/models` | List available AI models |
| GET | `/api/v1/ai/usage` | Get AI token usage stats |
| GET | `/api/v1/ai/providers/status` | Provider health status |
| POST | `/api/v1/ai/feedback` | Submit feedback on AI output |

**Streaming Completion Example:**

```json
// POST /api/v1/ai/completions/stream
// Request
{
    "task": "analyze_data",
    "messages": [
        {"role": "system", "content": "You are a data analyst."},
        {"role": "user", "content": "What trends do you see in this sales data?"}
    ],
    "context": {
        "dataset_id": "uuid",
        "columns": ["date", "revenue", "region"]
    },
    "config": {
        "model": "auto",
        "max_tokens": 2048,
        "stream": true
    }
}

// Response: Server-Sent Events stream
// data: {"type":"start","model":"gpt-4o","request_id":"req_123"}
// data: {"type":"content_delta","content":"Based on"}
// data: {"type":"content_delta","content":" the sales data"}
// data: {"type":"content_delta","content":", I can identify"}
// ...
// data: {"type":"done","usage":{"input_tokens":450,"output_tokens":380},"latency_ms":2100}
```

### 6.10 Billing Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/billing/plans` | List available plans |
| GET | `/api/v1/billing/subscription` | Get current subscription |
| POST | `/api/v1/billing/subscription` | Create/change subscription |
| DELETE | `/api/v1/billing/subscription` | Cancel subscription |
| GET | `/api/v1/billing/invoices` | List invoices |
| GET | `/api/v1/billing/invoices/{id}` | Get invoice details |
| GET | `/api/v1/billing/usage` | Get current period usage |
| POST | `/api/v1/billing/payment-method` | Add payment method |
| DELETE | `/api/v1/billing/payment-method/{id}` | Remove payment method |
| POST | `/api/v1/billing/webhook` | Stripe webhook handler |

### 6.11 WebSocket Event Catalog

**Connection**: `wss://api.daaas.io/ws/v1/?token={jwt_token}`

| Channel | Event | Direction | Description |
|---------|-------|-----------|-------------|
| `ai.stream` | `ai.chunk` | Server->Client | AI streaming token |
| `ai.stream` | `ai.done` | Server->Client | AI stream complete |
| `ai.stream` | `ai.cancel` | Client->Server | Cancel AI stream |
| `dataset.{id}` | `processing.progress` | Server->Client | Upload/processing progress |
| `dataset.{id}` | `processing.complete` | Server->Client | Processing finished |
| `model.{id}` | `training.progress` | Server->Client | Training epoch updates |
| `model.{id}` | `training.complete` | Server->Client | Training finished |
| `dashboard.{id}` | `data.updated` | Server->Client | Dashboard data refresh |
| `org.{id}` | `notification` | Server->Client | New notification |
| `session.{id}` | `collaboration.cursor` | Bidirectional | User cursor position |
| `session.{id}` | `collaboration.edit` | Bidirectional | Real-time edit |

### 6.12 Rate Limiting Tiers

| Plan | Requests/minute | Requests/hour | Burst |
|------|----------------|---------------|-------|
| Free | 30 | 500 | 10 |
| Starter | 120 | 5,000 | 30 |
| Professional | 600 | 30,000 | 100 |
| Enterprise | 3,000 | 150,000 | 500 |
| API Key | Configurable | Configurable | Configurable |

Rate limit headers returned on every response:
```
X-RateLimit-Limit: 120
X-RateLimit-Remaining: 115
X-RateLimit-Reset: 1704067200
X-RateLimit-Retry-After: 45
```


---

## 7. Frontend Architecture

### 7.1 React App Structure

```
frontend/
├── public/
│   ├── index.html
│   ├── favicon.ico
│   └── manifest.json
├── src/
│   ├── main.tsx                    # App entry point
│   ├── App.tsx                     # Root component with providers
│   ├── router.tsx                  # Route definitions
│   ├── vite-env.d.ts
│   │
│   ├── pages/                      # Page-level components (route targets)
│   │   ├── auth/
│   │   │   ├── LoginPage.tsx
│   │   │   ├── RegisterPage.tsx
│   │   │   ├── ForgotPasswordPage.tsx
│   │   │   └── OAuthCallbackPage.tsx
│   │   ├── dashboard/
│   │   │   ├── DashboardPage.tsx
│   │   │   └── DashboardBuilderPage.tsx
│   │   ├── datasets/
│   │   │   ├── DatasetListPage.tsx
│   │   │   ├── DatasetDetailPage.tsx
│   │   │   ├── DatasetUploadPage.tsx
│   │   │   └── DatasetCleaningPage.tsx
│   │   ├── analysis/
│   │   │   ├── AnalysisSessionPage.tsx
│   │   │   ├── StatisticalAnalysisPage.tsx
│   │   │   └── VisualizationBuilderPage.tsx
│   │   ├── models/
│   │   │   ├── ModelListPage.tsx
│   │   │   ├── ModelCreatePage.tsx
│   │   │   ├── ModelTrainingPage.tsx
│   │   │   └── ModelDeployPage.tsx
│   │   ├── reports/
│   │   │   ├── ReportListPage.tsx
│   │   │   └── ReportEditorPage.tsx
│   │   ├── settings/
│   │   │   ├── OrganizationSettingsPage.tsx
│   │   │   ├── BillingPage.tsx
│   │   │   ├── MembersPage.tsx
│   │   │   └── ApiKeysPage.tsx
│   │   └── NotFoundPage.tsx
│   │
│   ├── components/                 # Reusable UI components
│   │   ├── ui/                     # shadcn/ui base components
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   ├── Select.tsx
│   │   │   ├── Dialog.tsx
│   │   │   ├── Table.tsx
│   │   │   ├── Card.tsx
│   │   │   ├── Badge.tsx
│   │   │   ├── Toast.tsx
│   │   │   └── ...
│   │   ├── layout/
│   │   │   ├── AppShell.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Header.tsx
│   │   │   ├── Footer.tsx
│   │   │   └── Breadcrumbs.tsx
│   │   ├── data/
│   │   │   ├── DataTable.tsx
│   │   │   ├── DataGrid.tsx
│   │   │   ├── ColumnEditor.tsx
│   │   │   ├── FileUpload.tsx
│   │   │   └── DataPreview.tsx
│   │   ├── charts/
│   │   │   ├── ChartRenderer.tsx
│   │   │   ├── ChartConfigPanel.tsx
│   │   │   ├── BarChart.tsx
│   │   │   ├── LineChart.tsx
│   │   │   ├── ScatterPlot.tsx
│   │   │   ├── PieChart.tsx
│   │   │   ├── HeatMap.tsx
│   │   │   └── DashboardGrid.tsx
│   │   ├── ai/
│   │   │   ├── AIStreamingResponse.tsx
│   │   │   ├── AISuggestionCard.tsx
│   │   │   ├── AIOverrideEditor.tsx
│   │   │   ├── ModelSelector.tsx
│   │   │   └── TokenUsageBadge.tsx
│   │   ├── ml/
│   │   │   ├── ModelLeaderboard.tsx
│   │   │   ├── TrainingProgress.tsx
│   │   │   ├── ConfusionMatrix.tsx
│   │   │   ├── FeatureImportance.tsx
│   │   │   └── PredictionForm.tsx
│   │   └── common/
│   │       ├── LoadingSpinner.tsx
│   │       ├── ErrorBoundary.tsx
│   │       ├── EmptyState.tsx
│   │       ├── ConfirmDialog.tsx
│   │       └── Pagination.tsx
│   │
│   ├── hooks/                      # Custom React hooks
│   │   ├── useAuth.ts
│   │   ├── useOrganization.ts
│   │   ├── useDataset.ts
│   │   ├── useWebSocket.ts
│   │   ├── useAIStream.ts
│   │   ├── useFileUpload.ts
│   │   ├── useDebounce.ts
│   │   └── useLocalStorage.ts
│   │
│   ├── services/                   # API client and service layer
│   │   ├── api.ts                  # Axios instance configuration
│   │   ├── auth.service.ts
│   │   ├── dataset.service.ts
│   │   ├── analysis.service.ts
│   │   ├── visualization.service.ts
│   │   ├── model.service.ts
│   │   ├── report.service.ts
│   │   ├── ai.service.ts
│   │   ├── billing.service.ts
│   │   └── websocket.service.ts
│   │
│   ├── store/                      # Zustand state stores
│   │   ├── authStore.ts
│   │   ├── organizationStore.ts
│   │   ├── datasetStore.ts
│   │   ├── uiStore.ts
│   │   └── notificationStore.ts
│   │
│   ├── types/                      # TypeScript type definitions
│   │   ├── auth.types.ts
│   │   ├── dataset.types.ts
│   │   ├── analysis.types.ts
│   │   ├── model.types.ts
│   │   ├── billing.types.ts
│   │   └── api.types.ts
│   │
│   ├── utils/                      # Utility functions
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   ├── constants.ts
│   │   ├── chartHelpers.ts
│   │   └── errorHandlers.ts
│   │
│   └── styles/
│       ├── globals.css
│       └── tailwind.css
│
├── tailwind.config.ts
├── tsconfig.json
├── vite.config.ts
├── package.json
└── .env.example
```

### 7.2 State Management (Zustand)

```typescript
// Example: Auth Store
interface AuthState {
    user: User | null;
    accessToken: string | null;
    isAuthenticated: boolean;
    isLoading: boolean;

    // Actions
    login: (email: string, password: string) => Promise<void>;
    logout: () => void;
    refreshToken: () => Promise<void>;
    updateProfile: (data: Partial<User>) => Promise<void>;
}

// Example: Dataset Store
interface DatasetState {
    datasets: Dataset[];
    currentDataset: Dataset | null;
    uploadProgress: Record<string, number>;
    isLoading: boolean;

    // Actions
    fetchDatasets: () => Promise<void>;
    uploadDataset: (file: File) => Promise<void>;
    setCurrentDataset: (id: string) => void;
}
```

### 7.3 Routing Structure

```typescript
// Route Definitions
const routes = [
    { path: '/login', element: <LoginPage />, public: true },
    { path: '/register', element: <RegisterPage />, public: true },
    { path: '/oauth/callback/:provider', element: <OAuthCallbackPage />, public: true },

    // Protected routes (require authentication)
    { path: '/', element: <DashboardPage /> },
    { path: '/datasets', element: <DatasetListPage /> },
    { path: '/datasets/:id', element: <DatasetDetailPage /> },
    { path: '/datasets/:id/upload', element: <DatasetUploadPage /> },
    { path: '/datasets/:id/clean', element: <DatasetCleaningPage /> },
    { path: '/analysis', element: <AnalysisSessionPage /> },
    { path: '/analysis/:id', element: <StatisticalAnalysisPage /> },
    { path: '/visualizations', element: <VisualizationBuilderPage /> },
    { path: '/dashboards', element: <DashboardPage /> },
    { path: '/dashboards/:id/edit', element: <DashboardBuilderPage /> },
    { path: '/models', element: <ModelListPage /> },
    { path: '/models/create', element: <ModelCreatePage /> },
    { path: '/models/:id', element: <ModelTrainingPage /> },
    { path: '/models/:id/deploy', element: <ModelDeployPage /> },
    { path: '/reports', element: <ReportListPage /> },
    { path: '/reports/:id', element: <ReportEditorPage /> },
    { path: '/settings', element: <OrganizationSettingsPage /> },
    { path: '/settings/billing', element: <BillingPage /> },
    { path: '/settings/members', element: <MembersPage /> },
    { path: '/settings/api-keys', element: <ApiKeysPage /> },
];
```

### 7.4 Component Library

**Base**: Tailwind CSS 3.x + shadcn/ui (Radix UI primitives with Tailwind styling)

**Design System:**
- Color palette: Primary (blue), Secondary (slate), Accent (emerald), Danger (red)
- Typography: Inter for UI, JetBrains Mono for code/data
- Spacing: 4px grid system
- Border radius: Consistent rounding (sm: 4px, md: 8px, lg: 12px)
- Shadows: Subtle elevation system (sm, md, lg)
- Dark mode: Full dark mode support via Tailwind class strategy

### 7.5 Chart/Visualization Components

```typescript
// Unified Chart Renderer
interface ChartProps {
    type: 'bar' | 'line' | 'scatter' | 'pie' | 'heatmap' | 'box' | 'histogram';
    data: ChartData;
    config: ChartConfig;
    interactive?: boolean;
    onDataPointClick?: (point: DataPoint) => void;
    onBrushSelect?: (range: BrushRange) => void;
}

// ChartRenderer automatically selects Plotly or D3 based on chart type
const ChartRenderer: React.FC<ChartProps> = ({ type, data, config, ...props }) => {
    // Standard charts -> Plotly.js (simpler, faster)
    // Custom/complex charts -> D3.js (full control)
};
```

### 7.6 Real-time Updates via WebSocket

```typescript
// WebSocket hook for AI streaming
function useAIStream(taskType: string) {
    const [chunks, setChunks] = useState<string[]>([]);
    const [isStreaming, setIsStreaming] = useState(false);
    const [metadata, setMetadata] = useState<StreamMetadata | null>(null);

    const startStream = async (prompt: string, config?: AIConfig) => {
        setIsStreaming(true);
        setChunks([]);

        const ws = new WebSocket(`${WS_URL}/ai/stream/`);
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.type === 'content_delta') {
                setChunks(prev => [...prev, data.content]);
            } else if (data.type === 'done') {
                setIsStreaming(false);
                setMetadata(data.usage);
            }
        };

        ws.send(JSON.stringify({ task: taskType, prompt, config }));
    };

    const cancelStream = () => { /* send cancel message */ };

    return { chunks, fullText: chunks.join(''), isStreaming, metadata, startStream, cancelStream };
}
```

### 7.7 File Upload with Progress

```typescript
// Chunked upload with resume capability
function useFileUpload() {
    const [progress, setProgress] = useState(0);
    const [status, setStatus] = useState<'idle' | 'uploading' | 'processing' | 'complete' | 'error'>('idle');

    const upload = async (file: File, datasetId: string) => {
        const CHUNK_SIZE = 5 * 1024 * 1024; // 5MB chunks
        const totalChunks = Math.ceil(file.size / CHUNK_SIZE);

        for (let i = 0; i < totalChunks; i++) {
            const chunk = file.slice(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE);
            const formData = new FormData();
            formData.append('chunk', chunk);
            formData.append('chunk_index', String(i));
            formData.append('total_chunks', String(totalChunks));

            await api.post(`/datasets/${datasetId}/upload/chunk`, formData);
            setProgress(((i + 1) / totalChunks) * 100);
        }

        setStatus('processing');
        // Poll for processing completion or listen via WebSocket
    };

    return { upload, progress, status };
}
```

### 7.8 AI Streaming Response Display

The AI response component renders streamed tokens with a typing effect and supports markdown:

- Token-by-token rendering with smooth animation
- Markdown rendering (headers, lists, code blocks, tables)
- Code syntax highlighting
- Copy-to-clipboard for generated code
- Inline chart rendering for suggested visualizations
- Accept/Edit/Reject buttons below each AI suggestion
- Token count and cost display in real-time

---

## 8. Authentication and Multi-tenancy

### 8.1 JWT + Refresh Token Flow

```
┌─────────┐     ┌─────────────┐     ┌──────────┐
│  Client  │     │  API Server  │     │  Redis    │
└────┬─────┘     └──────┬───────┘     └────┬──────┘
     │                   │                   │
     │  POST /auth/login │                   │
     │──────────────────>│                   │
     │                   │ Verify credentials │
     │                   │ Generate tokens    │
     │                   │                   │
     │                   │  Store refresh     │
     │                   │──────────────────>│
     │                   │                   │
     │  {access, refresh}│                   │
     │<──────────────────│                   │
     │                   │                   │
     │  GET /api/resource│                   │
     │  Authorization:   │                   │
     │  Bearer {access}  │                   │
     │──────────────────>│                   │
     │                   │ Verify JWT (local) │
     │  200 {data}       │                   │
     │<──────────────────│                   │
     │                   │                   │
     │  POST /auth/refresh                   │
     │  {refresh_token}  │                   │
     │──────────────────>│                   │
     │                   │  Verify refresh   │
     │                   │──────────────────>│
     │                   │  Valid + rotate   │
     │                   │<──────────────────│
     │  {new_access,     │                   │
     │   new_refresh}    │                   │
     │<──────────────────│                   │
```

**Token Configuration:**
- Access token: RS256 signed, 15-minute expiry
- Refresh token: Opaque, 7-day expiry, stored in Redis
- Refresh rotation: New refresh token issued on each refresh (old invalidated)
- Token blacklist: Redis set for revoked access tokens (checked on sensitive operations)

### 8.2 OAuth2 Providers

| Provider | Scopes | Data Retrieved |
|----------|--------|----------------|
| Google | `openid email profile` | Email, name, avatar |
| GitHub | `user:email read:user` | Email, username, avatar |
| Microsoft | `openid email profile User.Read` | Email, name, avatar, org |

**OAuth Flow:**
1. Client redirects to `/api/v1/auth/oauth/{provider}/authorize`
2. Server generates state token, redirects to provider
3. User authorizes on provider's page
4. Provider redirects back to `/api/v1/auth/oauth/{provider}/callback`
5. Server exchanges code for tokens, fetches user info
6. If user exists: link account, return JWT
7. If new user: create account, prompt for organization name

### 8.3 Organization-Based Multi-tenancy

**Model**: Shared database with tenant isolation via organization_id foreign keys and Row-Level Security (RLS).

```sql
-- Enable RLS on all tenant tables
ALTER TABLE datasets ENABLE ROW LEVEL SECURITY;

-- Policy: Users can only see datasets in their organization
CREATE POLICY dataset_tenant_isolation ON datasets
    FOR ALL
    USING (organization_id IN (
        SELECT organization_id FROM memberships
        WHERE user_id = current_setting('app.current_user_id')::uuid
    ));
```

**Tenant Context**: Set via Django middleware on every request:
```python
class TenantMiddleware:
    def __call__(self, request):
        # Extract org from JWT claims or header
        org_id = request.auth.get('org_id')
        # Set PostgreSQL session variable for RLS
        with connection.cursor() as cursor:
            cursor.execute("SET app.current_user_id = %s", [str(request.user.id)])
            cursor.execute("SET app.current_org_id = %s", [str(org_id)])
        return self.get_response(request)
```

### 8.4 Role-Based Access Control (RBAC)

| Permission | Owner | Admin | Analyst | Viewer |
|------------|-------|-------|---------|--------|
| Manage billing | Yes | No | No | No |
| Delete organization | Yes | No | No | No |
| Manage members | Yes | Yes | No | No |
| Manage API keys | Yes | Yes | No | No |
| Create/edit datasets | Yes | Yes | Yes | No |
| Run ML training | Yes | Yes | Yes | No |
| Create reports | Yes | Yes | Yes | No |
| View all data | Yes | Yes | Yes | Yes |
| Export data | Yes | Yes | Yes | No |
| Delete resources | Yes | Yes | No | No |
| View dashboards | Yes | Yes | Yes | Yes |
| Edit dashboards | Yes | Yes | Yes | No |

**Implementation**: Django permission classes per view:
```python
class IsAnalystOrAbove(BasePermission):
    def has_permission(self, request, view):
        membership = request.user.get_membership(request.org_id)
        return membership.role in ('owner', 'admin', 'analyst')
```

### 8.5 API Key Management

- Keys generated with cryptographically secure random bytes
- Only hash stored in database (key shown once at creation)
- Key format: `daaas_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxx` (prefix for identification)
- Scopes: `read`, `write`, `admin`, `ml:predict`, `datasets:upload`
- Rate limiting applied per key
- Usage tracking per key (last used, request count)
- Expiration: Optional, default no expiry
- IP allowlist: Optional per-key restriction

### 8.6 Session Management

- Concurrent session limit: 5 devices per user
- Session list in user settings (device, location, last active)
- Remote session termination
- Forced logout on password change
- Suspicious login detection (new device, new location)
- Email notification on new login


---

## 9. Billing and Subscription Model

### 9.1 Plan Tiers

| Feature | Free | Starter ($49/mo) | Professional ($149/mo) | Enterprise (Custom) |
|---------|------|-------------------|------------------------|---------------------|
| **Datasets** | 3 | 25 | Unlimited | Unlimited |
| **Storage** | 500 MB | 10 GB | 100 GB | Custom (TB+) |
| **AI Tokens/month** | 50,000 | 500,000 | 5,000,000 | Unlimited |
| **ML Models** | 1 | 10 | 50 | Unlimited |
| **Team Members** | 1 | 5 | 25 | Unlimited |
| **Dashboards** | 2 | 20 | Unlimited | Unlimited |
| **Reports/month** | 5 | 50 | Unlimited | Unlimited |
| **Data Retention** | 30 days | 1 year | 5 years | Custom |
| **API Access** | No | Basic (100 req/hr) | Full (1000 req/hr) | Custom limits |
| **Support** | Community | Email (48h SLA) | Priority (4h SLA) | Dedicated (1h SLA) |
| **Collaboration** | No | Basic | Full (real-time) | Full + SSO |
| **Custom Branding** | No | No | Yes | Yes |
| **On-Premise** | No | No | No | Yes |
| **Audit Logs** | No | 30 days | 1 year | Unlimited |
| **SLA** | None | 99.5% | 99.9% | 99.99% |

### 9.2 Free Tier Details

The free tier allows users to experience the full platform with limited scale:
- 3 datasets, max 10,000 rows each
- 500 MB total storage
- 50,000 AI tokens per month (roughly 25 AI-powered operations)
- 1 ML model (training limited to 10 minutes)
- 2 dashboards with manual refresh only
- 5 AI-generated reports per month
- Single user only (no collaboration)
- Data deleted after 30 days of inactivity
- Community support via forums only
- "Powered by DAaaS" watermark on exports

### 9.3 Starter Tier ($49/month or $470/year)

Designed for small teams getting started with data analytics:
- 25 datasets, up to 1,000,000 rows each
- 10 GB storage with 90-day raw file retention
- 500,000 AI tokens (roughly 250 operations)
- 10 ML models with up to 1 hour training time each
- 5 team members with role-based access
- 20 dashboards with auto-refresh (minimum 5 minutes)
- 50 reports/month with PDF export
- Basic API access (100 requests/hour)
- Email support with 48-hour response SLA
- Basic collaboration (shared workspaces, comments)
- 30 days of audit logs

### 9.4 Professional Tier ($149/month or $1,430/year)

For growing companies with serious analytics needs:
- Unlimited datasets and rows
- 100 GB storage with intelligent tiering
- 5,000,000 AI tokens (roughly 2,500 operations)
- 50 ML models with GPU training (up to 4 hours each)
- 25 team members with full RBAC
- Unlimited dashboards with real-time updates
- Unlimited reports with scheduled delivery
- Full API access (1,000 requests/hour)
- Priority support with 4-hour response SLA
- Full collaboration with real-time cursors
- Custom branding on reports/dashboards
- 1 year of audit logs
- 99.9% uptime SLA
- Webhook integrations (Slack, Teams, email)
- Custom data connectors (1 included)

### 9.5 Enterprise Tier (Custom Pricing)

For organizations requiring maximum security and scale:
- Everything in Professional, plus:
- Unlimited everything (storage, tokens, models, members)
- Dedicated infrastructure (isolated compute)
- SSO/SAML integration
- On-premise deployment option
- Custom AI model fine-tuning
- Dedicated Customer Success Manager
- 1-hour response SLA
- 99.99% uptime SLA
- Unlimited audit log retention
- Custom compliance certifications (SOC 2, HIPAA, ISO 27001)
- Priority feature requests
- Custom data connectors (unlimited)
- White-label option
- Training and onboarding sessions

### 9.6 Usage-Based Add-ons

| Add-on | Unit | Price | Notes |
|--------|------|-------|-------|
| Extra AI Tokens | 100,000 tokens | $5 | Auto-purchase or manual |
| Extra Storage | 10 GB | $3/month | Auto-expands |
| GPU Compute | Per hour | $2/hour | For ML training |
| Extra API Calls | 1,000 calls | $1 | Above plan limit |
| Extra Team Members | Per user/month | $15 | Above plan limit |
| Dedicated Compute | Per instance/month | $200 | Isolated resources |

### 9.7 Stripe Integration Design

```python
# Stripe Integration Architecture
class StripeService:
    '''Handles all Stripe interactions.'''

    def create_customer(self, organization):
        '''Create Stripe customer for new organization.'''
        customer = stripe.Customer.create(
            email=organization.owner.email,
            name=organization.name,
            metadata={'org_id': str(organization.id)}
        )
        return customer.id

    def create_subscription(self, org, plan, billing_cycle):
        '''Create or update subscription.'''
        if billing_cycle == 'monthly':
            price_id = plan.stripe_price_id_monthly
        else:
            price_id = plan.stripe_price_id_yearly
        subscription = stripe.Subscription.create(
            customer=org.stripe_customer_id,
            items=[{'price': price_id}],
            metadata={'org_id': str(org.id), 'plan': plan.name}
        )
        return subscription

    def record_usage(self, org, metric, quantity):
        '''Report usage-based metering to Stripe.'''
        stripe.SubscriptionItem.create_usage_record(
            org.stripe_subscription_item_id,
            quantity=quantity,
            timestamp=int(time.time()),
            action='increment'
        )
```

### 9.8 Webhook Handling

Stripe webhooks handled at `POST /api/v1/billing/webhook`:

| Event | Action |
|-------|--------|
| `invoice.paid` | Activate subscription, reset usage counters |
| `invoice.payment_failed` | Send warning email, retry in 3 days |
| `customer.subscription.updated` | Sync plan changes |
| `customer.subscription.deleted` | Downgrade to free, disable features |
| `invoice.upcoming` | Send upcoming invoice notification |
| `charge.dispute.created` | Alert team, freeze account if needed |

### 9.9 Metering System

Usage tracked in real-time via Redis counters, persisted to PostgreSQL hourly:

```python
class UsageTracker:
    '''Tracks resource usage per organization.'''

    def track_ai_tokens(self, org_id, tokens):
        '''Increment AI token counter.'''
        key = f"usage:{org_id}:ai_tokens:{current_period()}"
        redis.incrby(key, tokens)

        # Check if approaching limit
        current = redis.get(key)
        limit = get_plan_limit(org_id, 'ai_tokens')

        if current >= limit * 0.95:
            send_budget_warning(org_id, 'ai_tokens', current, limit)
        if current >= limit:
            enforce_limit(org_id, 'ai_tokens')

    def get_current_usage(self, org_id):
        '''Get all usage metrics for current billing period.'''
        period = current_period()
        return {
            'ai_tokens': redis.get(f"usage:{org_id}:ai_tokens:{period}"),
            'storage_bytes': redis.get(f"usage:{org_id}:storage:{period}"),
            'compute_seconds': redis.get(f"usage:{org_id}:compute:{period}"),
            'api_calls': redis.get(f"usage:{org_id}:api_calls:{period}")
        }
```

---

## 10. Deployment and Infrastructure

### 10.1 Local Development (Docker Compose)

```yaml
# docker-compose.yml (simplified)
version: '3.9'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://daaas:daaas@postgres:5432/daaas
      - MONGODB_URL=mongodb://mongo:27017/daaas
      - REDIS_URL=redis://redis:6379/0
      - CELERY_BROKER_URL=redis://redis:6379/1
      - S3_ENDPOINT=http://minio:9000
      - DEBUG=true
    depends_on:
      - postgres
      - mongo
      - redis
      - minio

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    volumes:
      - ./frontend/src:/app/src
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=http://localhost:8000/api/v1

  celery-worker:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    command: celery -A daaas worker -l info -Q default,priority
    volumes:
      - ./backend:/app
    depends_on:
      - redis
      - postgres

  celery-beat:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    command: celery -A daaas beat -l info
    depends_on:
      - redis

  celery-ml-worker:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    command: celery -A daaas worker -l info -Q ml_training,data_processing -c 2
    volumes:
      - ./backend:/app
    depends_on:
      - redis

  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: daaas
      POSTGRES_USER: daaas
      POSTGRES_PASSWORD: daaas
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  mongo:
    image: mongo:7
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  minio:
    image: minio/minio
    command: server /data --console-address ":9001"
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    volumes:
      - minio_data:/data

  flower:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    command: celery -A daaas flower --port=5555
    ports:
      - "5555:5555"
    depends_on:
      - redis

volumes:
  postgres_data:
  mongo_data:
  minio_data:
```

### 10.2 Staging Environment

- Mirrors production architecture at smaller scale
- Deployed on every merge to `develop` branch
- Shared Kubernetes cluster with namespace isolation
- Seeded with anonymized production data subset
- Used for QA, integration testing, and demos
- Auto-deployed via GitHub Actions
- Accessible at `staging.daaas.io`

### 10.3 Production (Kubernetes on AWS)

```yaml
# High-level Kubernetes architecture
# Cluster: AWS EKS (managed Kubernetes)
#
# Namespace: daaas-production
#   - Deployment: api (Django, 3-10 replicas, HPA)
#   - Deployment: celery-default (3-8 replicas, HPA)
#   - Deployment: celery-ml (2-5 replicas, HPA on queue length)
#   - Deployment: celery-beat (1 replica, leader election)
#   - Deployment: websocket (Django Channels, 2-5 replicas)
#   - Deployment: frontend (Nginx + static files, 2-4 replicas)
#   - Service: api-service (ClusterIP)
#   - Service: websocket-service (ClusterIP)
#   - Ingress: main-ingress (ALB, TLS termination)
#   - CronJob: daily-cleanup
#   - CronJob: usage-aggregation
#   - CronJob: model-monitoring
#
# Namespace: daaas-data
#   - StatefulSet: postgresql (AWS RDS recommended for production)
#   - StatefulSet: mongodb (MongoDB Atlas recommended)
#   - StatefulSet: redis (AWS ElastiCache recommended)
#
# Namespace: daaas-monitoring
#   - Deployment: prometheus
#   - Deployment: grafana
#   - Deployment: loki
#   - DaemonSet: promtail
```

**AWS Services Used:**
- EKS: Kubernetes cluster management
- RDS: Managed PostgreSQL 16 (Multi-AZ)
- ElastiCache: Managed Redis 7 (cluster mode)
- S3: Object storage for datasets, models, exports
- CloudFront: CDN for frontend static assets
- Route53: DNS management
- ACM: TLS certificate management
- ECR: Docker image registry
- SQS: Dead letter queue for failed Celery tasks (optional)
- CloudWatch: Additional logging and alarms

### 10.4 CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Backend lint
        run: |
          pip install ruff black
          ruff check backend/
          black --check backend/
      - name: Frontend lint
        run: |
          cd frontend && npm ci
          npm run lint
          npm run type-check

  test-backend:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: test_daaas
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
      redis:
        image: redis:7-alpine
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: |
          pip install -e ".[test]"
          pytest --cov=daaas --cov-report=xml

  test-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: |
          cd frontend && npm ci
          npm run test -- --coverage

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Snyk security scan
        uses: snyk/actions/python@master
      - name: Trivy container scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'

  build:
    needs: [lint, test-backend, test-frontend, security-scan]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build and push images
        run: |
          docker build -t daaas-api:${GITHUB_SHA} ./backend
          docker build -t daaas-frontend:${GITHUB_SHA} ./frontend

  deploy-staging:
    needs: [build]
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: |
          kubectl set image deployment/api api=daaas-api:${GITHUB_SHA}
          kubectl rollout status deployment/api

  deploy-production:
    needs: [build]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Blue-green deploy
        run: echo "Deploy to green, smoke test, switch traffic"
```

### 10.5 Database Migrations Strategy

- Django migrations for PostgreSQL schema changes
- Migration files committed to version control
- Zero-downtime migrations (no DROP COLUMN without deprecation period)
- Large data migrations run as background Celery tasks
- MongoDB schema changes handled via application-level migration scripts
- Migration testing in CI against a production-like dataset
- Rollback procedure documented for every migration

### 10.6 Monitoring and Alerting

**Metrics Collected:**
- Request latency (p50, p95, p99) per endpoint
- Error rates (4xx, 5xx) per service
- Active users and concurrent sessions
- Database connection pool utilization
- Redis memory and hit rate
- Celery queue lengths and task execution times
- AI provider latency and error rates
- ML training duration and resource usage
- Storage utilization growth rate

**Alert Rules:**

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| API p99 latency | > 2s | > 5s | Scale up, investigate |
| Error rate | > 1% | > 5% | Page on-call engineer |
| Queue length | > 1000 | > 5000 | Scale workers |
| Disk usage | > 70% | > 85% | Expand storage |
| AI provider errors | > 5% | > 20% | Trigger fallback |
| Memory usage | > 80% | > 90% | Investigate leak |

### 10.7 Auto-scaling Policies

```yaml
# Horizontal Pod Autoscaler for API
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: "100"
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
        - type: Pods
          value: 2
          periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Pods
          value: 1
          periodSeconds: 120
```

### 10.8 Backup and Disaster Recovery

| Component | Backup Frequency | Retention | Recovery Time Objective |
|-----------|-----------------|-----------|------------------------|
| PostgreSQL | Continuous (WAL) + daily snapshot | 30 days | < 15 minutes |
| MongoDB | Every 6 hours | 14 days | < 30 minutes |
| Redis | Hourly RDB + AOF | 7 days | < 5 minutes |
| S3 Objects | Cross-region replication | Indefinite | < 1 hour |
| Kubernetes configs | GitOps (version controlled) | Indefinite | < 10 minutes |

**Disaster Recovery Plan:**
1. Multi-AZ deployment for all stateful services
2. Cross-region S3 replication for critical data
3. Database read replicas in secondary region
4. DNS failover via Route53 health checks
5. Automated runbook for region failover
6. Quarterly DR drills with documented results

### 10.9 Blue-Green Deployment

**Deployment Process:**
1. Deploy new version to Green environment
2. Run automated smoke tests against Green
3. Gradually shift traffic (10% -> 25% -> 50% -> 100%)
4. Monitor error rates at each step
5. If errors spike, immediately route all traffic back to Blue
6. After 24 hours stable on Green, decommission Blue
7. Green becomes the new Blue for next deployment


---

## 11. Security Considerations

### 11.1 Encryption

**In Transit:**
- TLS 1.3 enforced on all external connections
- HSTS headers with 1-year max-age and includeSubDomains
- Certificate pinning for mobile clients (future)
- Internal service mesh communication encrypted via Istio mTLS

**At Rest:**
- PostgreSQL: Transparent Data Encryption (TDE) via AWS RDS
- MongoDB: Encrypted storage engine (WiredTiger)
- S3: Server-side encryption (AES-256, SSE-S3 or SSE-KMS)
- Redis: In-memory (no disk encryption needed for cache-only data)
- Backups: Encrypted with separate KMS key
- Database connection strings and API keys: Encrypted in application config

**Application-Level Encryption:**
- Sensitive fields (OAuth tokens, API secrets) encrypted with AES-256-GCM before storage
- Encryption keys managed via AWS KMS or HashiCorp Vault
- Key rotation every 90 days with backward-compatible decryption
- PII fields hashed (email for lookup) or encrypted (names, addresses)

### 11.2 Input Validation and Sanitization

- All API inputs validated with Django REST Framework serializers
- Request body size limits (10MB general, 5GB for file uploads via chunked)
- SQL injection prevented via Django ORM parameterized queries
- NoSQL injection prevented via strict type checking on MongoDB queries
- File upload validation:
  - MIME type verification (not just extension)
  - File content scanning (magic bytes)
  - Maximum dimensions for images
  - Virus scanning via ClamAV integration
- HTML/script sanitization for user-generated text content
- URL validation for webhook endpoints (no internal IPs, no localhost)
- JSON schema validation for complex nested inputs

### 11.3 OWASP Top 10 Mitigations

| # | Vulnerability | Mitigation |
|---|--------------|------------|
| A01 | Broken Access Control | RBAC + RLS + middleware tenant checks |
| A02 | Cryptographic Failures | TLS 1.3, AES-256, proper key management |
| A03 | Injection | ORM parameterization, input validation |
| A04 | Insecure Design | Threat modeling, security reviews, least privilege |
| A05 | Security Misconfiguration | Infrastructure-as-code, security headers, no defaults |
| A06 | Vulnerable Components | Automated dependency scanning (Snyk, Dependabot) |
| A07 | Identity/Auth Failures | JWT with rotation, MFA support, rate-limited login |
| A08 | Software/Data Integrity | Signed deployments, dependency pinning, SRI for CDN |
| A09 | Security Logging Failures | Comprehensive audit logging, tamper-proof storage |
| A10 | Server-Side Request Forgery | URL allowlisting, no internal network access from user inputs |

### 11.4 Tenant Data Isolation

**Database Level:**
- Row-Level Security (RLS) policies on all tenant tables in PostgreSQL
- Every query automatically filtered by organization_id
- Separate MongoDB collections per dataset (dataset_rows_{dataset_id})
- Cross-tenant queries impossible at the database level

**Application Level:**
- Django middleware validates tenant context on every request
- All querysets automatically scoped to current organization
- File storage paths include organization_id prefix
- Cache keys namespaced by organization_id

**Infrastructure Level:**
- Enterprise tier gets dedicated database schemas or instances
- Network policies prevent pod-to-pod communication across tenant namespaces
- S3 bucket policies enforce organization-level access

### 11.5 GDPR/CCPA Compliance

- **Right to Access**: Export all user data via API endpoint
- **Right to Erasure**: Complete data deletion with cascade (30-day grace period)
- **Right to Portability**: Data export in standard formats (CSV, JSON)
- **Data Minimization**: Only collect necessary data, configurable retention
- **Consent Management**: Explicit opt-in for analytics, marketing, AI training
- **Data Processing Agreements**: Available for all plans
- **Sub-processor List**: Published and updated, notification on changes
- **Privacy Impact Assessments**: Conducted for new features touching PII
- **Cookie Policy**: Essential only by default, opt-in for analytics
- **Data Residency**: Option to choose data region (US, EU, APAC)
- **Breach Notification**: Automated detection, 72-hour notification process

### 11.6 Audit Logging

Every security-relevant action is logged with:
- Timestamp (UTC, millisecond precision)
- User ID and organization ID
- Action type (CRUD + custom actions)
- Resource type and ID
- Before/after state for modifications
- IP address and user agent
- Request ID for correlation
- Geolocation (derived from IP)

**Log Storage:**
- Real-time: Written to PostgreSQL audit_logs table (partitioned by month)
- Archive: Exported to S3 daily (immutable, encrypted)
- Retention: Per plan (30 days free, 1 year pro, unlimited enterprise)
- Tamper protection: Append-only with cryptographic chaining

### 11.7 Secrets Management

- **Development**: `.env` files (gitignored) with dotenv loading
- **Staging/Production**: AWS Secrets Manager or HashiCorp Vault
- **Rotation**: Automated rotation for database passwords, API keys
- **Access**: Kubernetes secrets injected as environment variables
- **No hardcoded secrets**: Pre-commit hook scans for secrets (gitleaks)
- **Least privilege**: Each service has only the secrets it needs
- **Emergency rotation**: Runbook for compromised credential response

### 11.8 File Upload Security

1. **Type Validation**: Check magic bytes, not just extension
2. **Size Limits**: Per-plan limits enforced at upload middleware
3. **Virus Scanning**: ClamAV scan before processing
4. **Sandboxed Processing**: File parsing in isolated containers
5. **No Execution**: Files stored with no-execute permissions
6. **Content Inspection**: Check for embedded scripts in CSV/Excel
7. **Quarantine**: Suspicious files quarantined for manual review
8. **Storage Isolation**: Each organization has isolated S3 prefix
9. **Signed URLs**: Time-limited, scoped download URLs (no direct S3 access)
10. **Filename Sanitization**: Strip special characters, limit length

### 11.9 Rate Limiting and DDoS Protection

**Application Level:**
- Per-user rate limits (Redis-backed sliding window)
- Per-IP rate limits for unauthenticated endpoints
- Per-organization aggregate limits
- Exponential backoff on repeated auth failures
- CAPTCHA after 5 failed login attempts

**Infrastructure Level:**
- AWS WAF with managed rule groups
- CloudFront with geographic restrictions (configurable)
- AWS Shield Standard (included) or Advanced (enterprise)
- Kubernetes network policies limiting pod connections
- Connection rate limiting at load balancer level

### 11.10 Dependency Vulnerability Scanning

- **Automated**: Dependabot/Snyk PRs for vulnerable dependencies
- **CI Gate**: Builds fail on critical/high severity CVEs
- **Weekly Audit**: Full dependency tree scan with trivy
- **SBOM Generation**: Software Bill of Materials for each release
- **License Compliance**: Automated license compatibility checking
- **Container Scanning**: Base image vulnerabilities detected in CI


---

## 12. Development Phases/Roadmap

### 12.1 Phase 1: MVP (Months 1-3)

**Goal**: Launch a functional platform that allows users to upload data, clean it with AI assistance, create basic visualizations, and generate simple reports.

#### Month 1: Foundation

| Week | Deliverables |
|------|-------------|
| 1 | Project setup: repo, CI/CD, Docker Compose, Django project scaffold, React app scaffold |
| 2 | Authentication system: registration, login, JWT, OAuth (Google), user profile |
| 3 | Organization and membership models, multi-tenancy middleware, RBAC basics |
| 4 | File upload service: chunked upload, S3 storage, basic format detection (CSV, Excel) |

#### Month 2: Core Data Features

| Week | Deliverables |
|------|-------------|
| 5 | Dataset management: CRUD, schema inference, column statistics, data preview |
| 6 | AI Gateway v1: OpenAI integration, basic prompt management, token counting |
| 7 | Data cleaning v1: AI-powered null detection, type mismatch detection, suggestions UI |
| 8 | Basic visualizations: bar, line, scatter, pie charts via Plotly integration |

#### Month 3: MVP Completion

| Week | Deliverables |
|------|-------------|
| 9 | Dashboard builder v1: grid layout, add charts, basic filtering |
| 10 | Report generation v1: AI generates markdown summary, PDF export |
| 11 | Billing integration: Stripe setup, free + starter plans, usage tracking |
| 12 | Polish, testing, documentation, beta launch preparation |

**Phase 1 Success Metrics:**
- 100 beta users registered
- Average session duration > 10 minutes
- 80% of users successfully upload and visualize data
- < 2 second average page load time
- Zero critical security vulnerabilities
- 99% uptime during beta

**Phase 1 Technical Milestones:**
- Django backend with 80%+ test coverage
- React frontend with all core pages functional
- CI/CD pipeline fully operational
- Staging and production environments deployed
- Monitoring and alerting configured
- API documentation (OpenAPI) published

### 12.2 Phase 2: Advanced Analytics (Months 4-5)

**Goal**: Add advanced statistical analysis, custom dashboards with real-time updates, collaboration features, and expand AI capabilities.

#### Month 4: Advanced Analysis

| Week | Deliverables |
|------|-------------|
| 13 | Statistical analysis module: descriptive stats, correlation matrix, hypothesis tests |
| 14 | AI Gateway v2: add Anthropic provider, fallback chain, streaming responses |
| 15 | Advanced visualizations: heatmaps, box plots, combination charts, D3.js custom charts |
| 16 | Dashboard v2: auto-refresh, cross-filtering, parameter controls, public sharing |

#### Month 5: Collaboration

| Week | Deliverables |
|------|-------------|
| 17 | Real-time collaboration: WebSocket infrastructure, shared cursors, live edits |
| 18 | Comments and activity feed, notification system (in-app + email) |
| 19 | Version history for datasets and analyses, diff view, rollback |
| 20 | Additional data connectors: PostgreSQL, MySQL direct connections, API ingestion |

**Phase 2 Success Metrics:**
- 500 active users
- 50% of users use collaboration features
- Average 3 dashboards per organization
- AI suggestion acceptance rate > 60%
- Multi-provider fallback reduces AI errors by 90%
- Net Promoter Score (NPS) > 30

**Phase 2 Technical Milestones:**
- WebSocket infrastructure with < 100ms latency
- Streaming AI responses functional end-to-end
- 3+ AI providers integrated and tested
- Database connection pooling handling 100+ concurrent connections
- Frontend bundle size < 500KB (gzipped)

### 12.3 Phase 3: ML Platform (Months 6-8)

**Goal**: Enable users to build, train, evaluate, and deploy machine learning models through an AutoML interface, with AI-guided feature engineering and model selection.

#### Month 6: ML Foundation

| Week | Deliverables |
|------|-------------|
| 21 | ML model definition: problem type selection, target/feature selection, data splitting |
| 22 | AutoML engine v1: algorithm selection, hyperparameter search (Optuna), parallel training |
| 23 | Training monitoring: real-time progress via WebSocket, metrics per epoch, early stopping |
| 24 | Model evaluation: confusion matrix, ROC curves, feature importance, SHAP values |

#### Month 7: Model Deployment

| Week | Deliverables |
|------|-------------|
| 25 | Model versioning and registry, artifact storage in S3 |
| 26 | Prediction API: REST endpoint for single and batch predictions |
| 27 | Model monitoring: data drift detection, performance degradation alerts |
| 28 | AI-powered feature engineering: AI suggests transformations and new features |

#### Month 8: Advanced ML

| Week | Deliverables |
|------|-------------|
| 29 | Time series forecasting: Prophet integration, ARIMA, seasonal decomposition |
| 30 | NLP capabilities: text classification, sentiment analysis, named entity recognition |
| 31 | A/B testing for models, automated retraining pipelines |
| 32 | ML documentation generation, model cards, compliance reports |

**Phase 3 Success Metrics:**
- 1,000 active users
- 200+ ML models trained by users
- Model training completion rate > 85%
- Average prediction API latency < 50ms
- 30% of users deploy at least one model
- Platform handles 1M+ predictions per day

**Phase 3 Technical Milestones:**
- AutoML pipeline supporting 6+ algorithm families
- GPU-accelerated training option
- Model serving with < 50ms p99 latency
- Horizontal scaling of prediction endpoints
- Model artifact versioning and rollback
- Automated data drift detection pipeline

### 12.4 Phase 4: Enterprise (Months 9-10)

**Goal**: Add enterprise-grade features including SSO, advanced security, comprehensive audit trails, custom integrations, and self-hosted deployment options.

#### Month 9: Enterprise Security

| Week | Deliverables |
|------|-------------|
| 33 | SSO/SAML integration: Okta, Azure AD, OneLogin support |
| 34 | Advanced audit logging: complete action trail, tamper-proof storage, export |
| 35 | IP allowlisting, session controls, MFA enforcement, security policies |
| 36 | SOC 2 compliance documentation, penetration testing, vulnerability remediation |

#### Month 10: Enterprise Features

| Week | Deliverables |
|------|-------------|
| 37 | Custom data connectors framework: pluggable adapter system |
| 38 | Advanced API: GraphQL option, bulk operations, async endpoints |
| 39 | White-label and custom branding, embedded analytics (iframe SDK) |
| 40 | Self-hosted deployment: Helm chart, installation guide, air-gapped support |

**Phase 4 Success Metrics:**
- 5 enterprise customers signed
- SOC 2 Type II certification achieved
- Self-hosted deployment in < 2 hours
- 99.99% uptime achieved
- Zero data breaches
- Enterprise customer retention > 95%

**Phase 4 Technical Milestones:**
- SAML 2.0 and OIDC support fully tested
- Helm chart with one-command deployment
- Multi-region deployment capability
- Sub-100ms API response times at p99
- Complete API coverage via SDK (Python, JavaScript)
- Comprehensive security scanning in CI

### 12.5 Future Roadmap (Beyond Phase 4)

- **AI Fine-tuning**: Allow organizations to fine-tune AI models on their data
- **Marketplace**: Plugin marketplace for custom visualizations, connectors, models
- **Mobile App**: iOS/Android app for viewing dashboards and receiving alerts
- **Embedded Analytics**: JavaScript SDK for embedding charts in external apps
- **Data Catalog**: Organization-wide data governance and discovery
- **Advanced NLP**: Natural language querying of datasets ("show me sales by region")
- **Real-time Streaming Analytics**: Process and visualize streaming data sources
- **Jupyter Integration**: Embed Jupyter notebooks for advanced users


---

## 13. File/Folder Structure

### 13.1 Complete Project Tree

```
daaas-platform/
├── PLAN.md                              # This document
├── README.md                            # Project overview and quick start
├── CONTRIBUTING.md                      # Contribution guidelines
├── LICENSE                              # License file
├── docker-compose.yml                   # Local development stack
├── docker-compose.prod.yml              # Production overrides
├── Makefile                             # Common development commands
├── .env.example                         # Environment variable template
├── .gitignore                           # Git ignore rules
├── .pre-commit-config.yaml              # Pre-commit hooks configuration
│
├── backend/                             # Django backend application
│   ├── Dockerfile                       # Production Docker image
│   ├── Dockerfile.dev                   # Development Docker image (with hot-reload)
│   ├── pyproject.toml                   # Python project configuration (dependencies, tools)
│   ├── poetry.lock                      # Locked dependencies
│   ├── manage.py                        # Django management script
│   ├── conftest.py                      # Global pytest fixtures
│   ├── pytest.ini                       # Pytest configuration
│   │
│   ├── daaas/                           # Django project root
│   │   ├── __init__.py
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py                  # Shared settings
│   │   │   ├── development.py           # Dev-specific settings
│   │   │   ├── staging.py              # Staging settings
│   │   │   ├── production.py           # Production settings
│   │   │   └── test.py                 # Test settings
│   │   ├── urls.py                      # Root URL configuration
│   │   ├── wsgi.py                      # WSGI entry point
│   │   ├── asgi.py                      # ASGI entry point (WebSockets)
│   │   └── celery.py                    # Celery app configuration
│   │
│   ├── apps/                            # Django applications
│   │   ├── __init__.py
│   │   │
│   │   ├── accounts/                    # User management and authentication
│   │   │   ├── __init__.py
│   │   │   ├── models.py               # User, OAuthConnection models
│   │   │   ├── serializers.py          # DRF serializers
│   │   │   ├── views.py               # Auth views (login, register, OAuth)
│   │   │   ├── urls.py                # Auth URL patterns
│   │   │   ├── permissions.py         # Custom permission classes
│   │   │   ├── backends.py            # Custom auth backends
│   │   │   ├── tokens.py             # JWT token utilities
│   │   │   ├── signals.py            # User-related signals
│   │   │   ├── admin.py              # Admin configuration
│   │   │   ├── tests/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── test_models.py
│   │   │   │   ├── test_views.py
│   │   │   │   ├── test_serializers.py
│   │   │   │   └── factories.py       # Test factories (factory_boy)
│   │   │   └── migrations/
│   │   │
│   │   ├── organizations/              # Multi-tenancy and team management
│   │   │   ├── __init__.py
│   │   │   ├── models.py              # Organization, Membership models
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── middleware.py          # Tenant context middleware
│   │   │   ├── permissions.py         # Role-based permissions
│   │   │   ├── signals.py
│   │   │   ├── admin.py
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── datasets/                   # Data upload, management, cleaning
│   │   │   ├── __init__.py
│   │   │   ├── models.py             # Dataset, DatasetVersion, DataColumn models
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── upload.py          # File upload handling
│   │   │   │   ├── schema_inference.py # Column type detection
│   │   │   │   ├── cleaning.py        # Data cleaning operations
│   │   │   │   ├── profiling.py       # Data profiling/statistics
│   │   │   │   └── connectors.py      # External data source connectors
│   │   │   ├── tasks.py              # Celery tasks (processing, sync)
│   │   │   ├── admin.py
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── analytics/                  # Analysis sessions and statistical analysis
│   │   │   ├── __init__.py
│   │   │   ├── models.py             # AnalysisSession, AnalysisStep models
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── statistics.py      # Statistical analysis functions
│   │   │   │   ├── correlation.py     # Correlation analysis
│   │   │   │   ├── hypothesis.py      # Hypothesis testing
│   │   │   │   └── time_series.py     # Time series analysis
│   │   │   ├── tasks.py
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── visualizations/            # Charts, dashboards, exports
│   │   │   ├── __init__.py
│   │   │   ├── models.py             # Visualization, Dashboard, Widget models
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── chart_builder.py   # Chart configuration and data
│   │   │   │   ├── export.py          # PNG/SVG/PDF export
│   │   │   │   └── suggestions.py     # AI chart suggestions
│   │   │   ├── tasks.py
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── ml/                         # Machine learning models and training
│   │   │   ├── __init__.py
│   │   │   ├── models.py             # MLModel, TrainingRun, ModelVersion, Prediction
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── automl.py          # AutoML pipeline orchestration
│   │   │   │   ├── training.py        # Model training execution
│   │   │   │   ├── evaluation.py      # Model evaluation and metrics
│   │   │   │   ├── prediction.py      # Inference service
│   │   │   │   ├── feature_engineering.py  # Feature creation and selection
│   │   │   │   ├── monitoring.py      # Drift detection, performance monitoring
│   │   │   │   └── explainability.py  # SHAP, feature importance
│   │   │   ├── tasks.py              # Training tasks (long-running)
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── reports/                    # Report generation and management
│   │   │   ├── __init__.py
│   │   │   ├── models.py             # Report, ReportSection models
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── generator.py       # AI report generation
│   │   │   │   ├── templates.py       # Report templates
│   │   │   │   └── export.py          # PDF/Word export
│   │   │   ├── tasks.py
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── ai_gateway/                # AI provider abstraction and gateway
│   │   │   ├── __init__.py
│   │   │   ├── models.py             # AIGeneration log model
│   │   │   ├── serializers.py
│   │   │   ├── views.py             # Gateway API endpoints
│   │   │   ├── urls.py
│   │   │   ├── providers/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py           # Abstract provider interface
│   │   │   │   ├── openai.py         # OpenAI adapter
│   │   │   │   ├── anthropic.py      # Anthropic adapter
│   │   │   │   ├── groq.py           # Groq adapter
│   │   │   │   ├── ollama.py         # Ollama adapter
│   │   │   │   └── openai_compatible.py  # Generic OpenAI-compatible adapter
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── router.py         # Request routing logic
│   │   │   │   ├── fallback.py       # Fallback chain management
│   │   │   │   ├── streaming.py      # Stream management
│   │   │   │   ├── cache.py          # Semantic response cache
│   │   │   │   ├── token_counter.py  # Token counting utilities
│   │   │   │   └── health.py         # Provider health checks
│   │   │   ├── prompts/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── manager.py        # Prompt template management
│   │   │   │   ├── templates/        # Prompt template files (YAML/JSON)
│   │   │   │   │   ├── data_cleaning.yaml
│   │   │   │   │   ├── visualization.yaml
│   │   │   │   │   ├── analysis.yaml
│   │   │   │   │   ├── report.yaml
│   │   │   │   │   └── ml.yaml
│   │   │   │   └── variables.py      # Template variable injection
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── billing/                   # Subscriptions, usage, invoicing
│   │   │   ├── __init__.py
│   │   │   ├── models.py            # Plan, Subscription, UsageRecord, Invoice
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── stripe_service.py  # Stripe API integration
│   │   │   │   ├── metering.py        # Usage metering and tracking
│   │   │   │   ├── limits.py          # Plan limit enforcement
│   │   │   │   └── webhooks.py        # Stripe webhook handlers
│   │   │   ├── tasks.py              # Usage aggregation tasks
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   ├── notifications/            # Notifications and activity
│   │   │   ├── __init__.py
│   │   │   ├── models.py            # Notification, ActivityLog models
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── sender.py         # Multi-channel notification sender
│   │   │   │   └── email.py          # Email notification templates
│   │   │   ├── tests/
│   │   │   └── migrations/
│   │   │
│   │   └── audit/                     # Audit logging
│   │       ├── __init__.py
│   │       ├── models.py            # AuditLog model
│   │       ├── middleware.py        # Automatic audit logging middleware
│   │       ├── serializers.py
│   │       ├── views.py
│   │       ├── urls.py
│   │       ├── tests/
│   │       └── migrations/
│   │
│   ├── core/                          # Shared utilities and base classes
│   │   ├── __init__.py
│   │   ├── models.py                # Base model with timestamps, UUID PK
│   │   ├── pagination.py           # Custom cursor pagination
│   │   ├── exceptions.py           # Custom exception classes
│   │   ├── throttling.py           # Custom rate limiting
│   │   ├── renderers.py            # Custom response renderers
│   │   ├── middleware/
│   │   │   ├── __init__.py
│   │   │   ├── tenant.py           # Tenant context middleware
│   │   │   ├── audit.py            # Audit logging middleware
│   │   │   └── request_id.py       # Request ID injection
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── encryption.py        # Field-level encryption utilities
│   │       ├── validators.py        # Shared validators
│   │       ├── storage.py           # S3 storage utilities
│   │       └── helpers.py           # General helper functions
│   │
│   └── websockets/                    # Django Channels consumers
│       ├── __init__.py
│       ├── routing.py               # WebSocket URL routing
│       ├── middleware.py            # WebSocket auth middleware
│       ├── consumers/
│       │   ├── __init__.py
│       │   ├── ai_stream.py         # AI streaming consumer
│       │   ├── collaboration.py     # Real-time collaboration consumer
│       │   ├── notifications.py     # Notification delivery consumer
│       │   └── progress.py          # Task progress consumer
│       └── tests/
│
├── frontend/                          # React frontend application
│   ├── Dockerfile                    # Production Docker image (Nginx)
│   ├── Dockerfile.dev               # Development Docker image (Vite)
│   ├── nginx.conf                   # Nginx configuration for production
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
│   ├── tailwind.config.ts
│   ├── postcss.config.js
│   ├── .eslintrc.cjs
│   ├── .prettierrc
│   ├── index.html
│   │
│   ├── public/
│   │   ├── favicon.ico
│   │   ├── robots.txt
│   │   └── manifest.json
│   │
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── router.tsx
│   │   ├── vite-env.d.ts
│   │   ├── pages/                   # (see Section 7.1 for full breakdown)
│   │   ├── components/              # (see Section 7.1 for full breakdown)
│   │   ├── hooks/                   # (see Section 7.1 for full breakdown)
│   │   ├── services/               # (see Section 7.1 for full breakdown)
│   │   ├── store/                  # (see Section 7.1 for full breakdown)
│   │   ├── types/                  # (see Section 7.1 for full breakdown)
│   │   ├── utils/                  # (see Section 7.1 for full breakdown)
│   │   └── styles/
│   │       ├── globals.css
│   │       └── tailwind.css
│   │
│   └── tests/
│       ├── setup.ts                 # Test setup (vitest)
│       ├── utils.tsx                # Test utilities (render helpers)
│       └── __mocks__/              # Module mocks
│
├── infrastructure/                    # Infrastructure as Code
│   ├── docker/
│   │   ├── backend/
│   │   │   ├── Dockerfile
│   │   │   └── entrypoint.sh
│   │   ├── frontend/
│   │   │   ├── Dockerfile
│   │   │   └── nginx.conf
│   │   └── nginx/
│   │       └── default.conf         # Reverse proxy for local dev
│   │
│   ├── kubernetes/
│   │   ├── base/                    # Base K8s manifests
│   │   │   ├── namespace.yaml
│   │   │   ├── api-deployment.yaml
│   │   │   ├── api-service.yaml
│   │   │   ├── celery-deployment.yaml
│   │   │   ├── websocket-deployment.yaml
│   │   │   ├── frontend-deployment.yaml
│   │   │   ├── ingress.yaml
│   │   │   ├── hpa.yaml
│   │   │   ├── configmap.yaml
│   │   │   └── secrets.yaml
│   │   ├── overlays/
│   │   │   ├── staging/
│   │   │   │   └── kustomization.yaml
│   │   │   └── production/
│   │   │       └── kustomization.yaml
│   │   └── kustomization.yaml
│   │
│   ├── terraform/                   # Cloud infrastructure provisioning
│   │   ├── environments/
│   │   │   ├── staging/
│   │   │   │   ├── main.tf
│   │   │   │   ├── variables.tf
│   │   │   │   └── terraform.tfvars
│   │   │   └── production/
│   │   │       ├── main.tf
│   │   │       ├── variables.tf
│   │   │       └── terraform.tfvars
│   │   ├── modules/
│   │   │   ├── eks/                 # EKS cluster module
│   │   │   ├── rds/                 # RDS PostgreSQL module
│   │   │   ├── elasticache/         # Redis module
│   │   │   ├── s3/                  # S3 buckets module
│   │   │   ├── ecr/                 # Container registry module
│   │   │   └── monitoring/          # CloudWatch/Prometheus module
│   │   └── backend.tf              # Terraform state backend
│   │
│   └── helm/                        # Helm chart for self-hosted deployment
│       └── daaas/
│           ├── Chart.yaml
│           ├── values.yaml
│           ├── values.production.yaml
│           └── templates/
│               ├── deployment.yaml
│               ├── service.yaml
│               ├── ingress.yaml
│               ├── configmap.yaml
│               └── secrets.yaml
│
├── .github/                          # GitHub configuration
│   ├── workflows/
│   │   ├── ci.yml                   # Lint + test on PR
│   │   ├── cd-staging.yml           # Deploy to staging on develop merge
│   │   ├── cd-production.yml        # Deploy to production on main merge
│   │   ├── security-scan.yml        # Weekly security scanning
│   │   └── dependency-update.yml    # Automated dependency updates
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── config.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
│
├── docs/                             # Project documentation
│   ├── architecture/
│   │   ├── overview.md              # Architecture decision records
│   │   ├── ai-gateway.md           # AI gateway detailed design
│   │   ├── data-pipeline.md        # Data processing pipeline
│   │   └── diagrams/               # Architecture diagrams (Mermaid/PlantUML)
│   ├── api/
│   │   ├── openapi.yaml            # OpenAPI 3.0 specification
│   │   └── websocket-events.md     # WebSocket event documentation
│   ├── deployment/
│   │   ├── local-setup.md          # Local development guide
│   │   ├── staging.md              # Staging deployment guide
│   │   ├── production.md           # Production deployment guide
│   │   └── self-hosted.md          # Self-hosted installation guide
│   ├── guides/
│   │   ├── getting-started.md      # User getting started guide
│   │   ├── data-upload.md          # Data upload documentation
│   │   ├── ml-models.md            # ML model training guide
│   │   └── api-usage.md            # API usage examples
│   └── runbooks/
│       ├── incident-response.md    # Incident response procedures
│       ├── database-recovery.md    # Database recovery procedures
│       └── scaling.md              # Scaling procedures
│
├── scripts/                          # Development and operational scripts
│   ├── setup-dev.sh                 # Local development setup
│   ├── seed-data.py                 # Database seeding for development
│   ├── generate-api-docs.sh        # OpenAPI spec generation
│   ├── run-migrations.sh           # Migration runner with safety checks
│   ├── backup-database.sh          # Manual backup trigger
│   └── load-test.py                # Load testing script (locust)
│
└── tests/                            # Integration and E2E tests
    ├── integration/
    │   ├── test_upload_pipeline.py  # Full upload-to-visualization test
    │   ├── test_ml_pipeline.py      # Full ML training pipeline test
    │   └── test_ai_gateway.py       # AI gateway integration test
    └── e2e/
        ├── playwright.config.ts     # Playwright E2E test config
        ├── tests/
        │   ├── auth.spec.ts         # Authentication E2E tests
        │   ├── dataset.spec.ts      # Dataset upload E2E tests
        │   └── dashboard.spec.ts    # Dashboard builder E2E tests
        └── fixtures/
            └── sample-data/         # Sample datasets for testing
                ├── sales.csv
                ├── customers.xlsx
                └── timeseries.json
```

---

## Summary

This document outlines the complete architecture, design decisions, and implementation roadmap for the DAaaS (Data Analytics as a Service) platform. Key principles guiding the project:

1. **HYBRID AI**: AI handles complexity; users maintain full control and can override any AI output
2. **Multi-Provider**: No vendor lock-in; best-in-class AI for each task type with automatic fallback
3. **End-to-End**: Single platform from raw data to deployed ML models and executive reports
4. **Enterprise-Ready**: Multi-tenant, secure, compliant, scalable from day one
5. **Developer-First**: API-first design, comprehensive documentation, self-hosted option
6. **Iterative Delivery**: MVP in 3 months, full platform in 10 months, continuous improvement thereafter

The phased approach ensures we deliver value early while building toward a comprehensive analytics platform that competes with enterprise tools at a fraction of the cost.

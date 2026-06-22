#!/bin/bash

# Analyze the repository history for Project 3's feature-branch workflow.
# This script is informational and always exits successfully so students can
# still receive testing feedback even when their Git workflow needs work.

set -uo pipefail

BAD_MESSAGE_PATTERN='^(wip|update|stuff|temp|asdf|final|final final|fix)$'
CONVENTIONAL_PATTERN='^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(.+\))?!?:'
EXPECTED_BRANCHES=(
    "feature/config-loader"
    "feature/pipeline-parser"
    "feature/metrics-calculator"
    "feature/anomaly-detection"
    "feature/report-generation"
    "feature/cli-interface"
)

echo "🔍 Analyzing Git workflow for Project 3..."
echo ""

CURRENT_BRANCH=$(git branch --show-current 2>/dev/null || true)
if [ -z "$CURRENT_BRANCH" ]; then
    CURRENT_BRANCH="detached"
fi

if git show-ref --verify --quiet refs/heads/main; then
    HISTORY_REF="main"
else
    HISTORY_REF="HEAD"
fi

echo "Inspecting commit history from: $HISTORY_REF"

COMMIT_MESSAGES=$(git log "$HISTORY_REF" --no-merges --pretty="%s" 2>/dev/null || true)
ALL_BRANCH_REFS=$(git for-each-ref --format='%(refname:short)' refs/heads refs/remotes/origin 2>/dev/null \
    | grep -v '^origin/HEAD$' \
    | sort -u || true)
FEATURE_BRANCHES=$(printf '%s\n' "$ALL_BRANCH_REFS" | grep -E '(^|/)feature/' || true)

if [ -n "$COMMIT_MESSAGES" ]; then
    COMMIT_COUNT=$(printf '%s\n' "$COMMIT_MESSAGES" | wc -l | tr -d ' ')
    CONVENTIONAL_COUNT=$(printf '%s\n' "$COMMIT_MESSAGES" | grep -Ec "$CONVENTIONAL_PATTERN" || true)
    BAD_MESSAGE_COUNT=$(printf '%s\n' "$COMMIT_MESSAGES" | grep -Eic "$BAD_MESSAGE_PATTERN" || true)
else
    COMMIT_COUNT=0
    CONVENTIONAL_COUNT=0
    BAD_MESSAGE_COUNT=0
fi

if [ -n "$FEATURE_BRANCHES" ]; then
    FEATURE_BRANCH_COUNT=$(printf '%s\n' "$FEATURE_BRANCHES" | wc -l | tr -d ' ')
else
    FEATURE_BRANCH_COUNT=0
fi

REQUIRED_BRANCH_COUNT=0
MERGED_REQUIRED_COUNT=0
MISSING_REQUIRED_BRANCHES=()
PRESENT_REQUIRED_BRANCHES=()
MERGED_REQUIRED_BRANCHES=()

for branch in "${EXPECTED_BRANCHES[@]}"; do
    branch_ref=""

    if git show-ref --verify --quiet "refs/heads/$branch"; then
        branch_ref="$branch"
    elif git show-ref --verify --quiet "refs/remotes/origin/$branch"; then
        branch_ref="origin/$branch"
    fi

    if [ -n "$branch_ref" ]; then
        REQUIRED_BRANCH_COUNT=$((REQUIRED_BRANCH_COUNT + 1))
        PRESENT_REQUIRED_BRANCHES+=("$branch")

        if git merge-base --is-ancestor "$branch_ref" "$HISTORY_REF" 2>/dev/null; then
            MERGED_REQUIRED_COUNT=$((MERGED_REQUIRED_COUNT + 1))
            MERGED_REQUIRED_BRANCHES+=("$branch")
        fi
    else
        MISSING_REQUIRED_BRANCHES+=("$branch")
    fi
done

BRANCH_HISTORY_PRESENT="no"
if [ -f branch_history.txt ]; then
    BRANCH_HISTORY_PRESENT="yes"
fi

LAST_FIVE_MESSAGES=$(git log "$HISTORY_REF" --no-merges --pretty="- %s" -5 2>/dev/null || true)

COMMIT_COUNT_TARGET=10
COMMIT_COUNT_MET="no"
if [ "$COMMIT_COUNT" -ge "$COMMIT_COUNT_TARGET" ]; then
    COMMIT_COUNT_MET="yes"
fi

COMMIT_QUALITY_MET="no"
if [ "$BAD_MESSAGE_COUNT" -eq 0 ]; then
    COMMIT_QUALITY_MET="yes"
fi

TASK_CONFIG_LOADER_PRESENT="no"
TASK_CONFIG_LOADER_MERGED="no"
TASK_PIPELINE_PARSER_PRESENT="no"
TASK_PIPELINE_PARSER_MERGED="no"
TASK_METRICS_CALCULATOR_PRESENT="no"
TASK_METRICS_CALCULATOR_MERGED="no"
TASK_ANOMALY_DETECTION_PRESENT="no"
TASK_ANOMALY_DETECTION_MERGED="no"
TASK_REPORT_GENERATION_PRESENT="no"
TASK_REPORT_GENERATION_MERGED="no"
TASK_CLI_INTERFACE_PRESENT="no"
TASK_CLI_INTERFACE_MERGED="no"

for branch in "${PRESENT_REQUIRED_BRANCHES[@]}"; do
    case "$branch" in
        feature/config-loader)
            TASK_CONFIG_LOADER_PRESENT="yes"
            ;;
        feature/pipeline-parser)
            TASK_PIPELINE_PARSER_PRESENT="yes"
            ;;
        feature/metrics-calculator)
            TASK_METRICS_CALCULATOR_PRESENT="yes"
            ;;
        feature/anomaly-detection)
            TASK_ANOMALY_DETECTION_PRESENT="yes"
            ;;
        feature/report-generation)
            TASK_REPORT_GENERATION_PRESENT="yes"
            ;;
        feature/cli-interface)
            TASK_CLI_INTERFACE_PRESENT="yes"
            ;;
    esac
done

for branch in "${MERGED_REQUIRED_BRANCHES[@]}"; do
    case "$branch" in
        feature/config-loader)
            TASK_CONFIG_LOADER_MERGED="yes"
            ;;
        feature/pipeline-parser)
            TASK_PIPELINE_PARSER_MERGED="yes"
            ;;
        feature/metrics-calculator)
            TASK_METRICS_CALCULATOR_MERGED="yes"
            ;;
        feature/anomaly-detection)
            TASK_ANOMALY_DETECTION_MERGED="yes"
            ;;
        feature/report-generation)
            TASK_REPORT_GENERATION_MERGED="yes"
            ;;
        feature/cli-interface)
            TASK_CLI_INTERFACE_MERGED="yes"
            ;;
    esac
done

join_items() {
    local separator="$1"
    shift

    if [ "$#" -eq 0 ]; then
        echo "none"
        return
    fi

    local joined="$1"
    shift

    local item
    for item in "$@"; do
        joined="${joined}${separator}${item}"
    done

    echo "$joined"
}

if [ "$REQUIRED_BRANCH_COUNT" -gt 0 ]; then
    PRESENT_REQUIRED_JOINED=$(join_items ', ' "${PRESENT_REQUIRED_BRANCHES[@]}")
else
    PRESENT_REQUIRED_JOINED="none"
fi

if [ "$MERGED_REQUIRED_COUNT" -gt 0 ]; then
    MERGED_REQUIRED_JOINED=$(join_items ', ' "${MERGED_REQUIRED_BRANCHES[@]}")
else
    MERGED_REQUIRED_JOINED="none"
fi

if [ "${#MISSING_REQUIRED_BRANCHES[@]}" -gt 0 ]; then
    MISSING_REQUIRED_JOINED=$(join_items ', ' "${MISSING_REQUIRED_BRANCHES[@]}")
else
    MISSING_REQUIRED_JOINED="none"
fi

if [ -n "${GITHUB_OUTPUT:-}" ]; then
    {
        echo "current_branch=$CURRENT_BRANCH"
        echo "history_ref=$HISTORY_REF"
        echo "commit_count=$COMMIT_COUNT"
        echo "conventional_count=$CONVENTIONAL_COUNT"
        echo "bad_message_count=$BAD_MESSAGE_COUNT"
        echo "feature_branch_count=$FEATURE_BRANCH_COUNT"
        echo "required_branch_count=$REQUIRED_BRANCH_COUNT"
        echo "merged_required_count=$MERGED_REQUIRED_COUNT"
        echo "branch_history_present=$BRANCH_HISTORY_PRESENT"
        echo "commit_count_target=$COMMIT_COUNT_TARGET"
        echo "commit_count_met=$COMMIT_COUNT_MET"
        echo "commit_quality_met=$COMMIT_QUALITY_MET"
        echo "task_config_loader_present=$TASK_CONFIG_LOADER_PRESENT"
        echo "task_config_loader_merged=$TASK_CONFIG_LOADER_MERGED"
        echo "task_pipeline_parser_present=$TASK_PIPELINE_PARSER_PRESENT"
        echo "task_pipeline_parser_merged=$TASK_PIPELINE_PARSER_MERGED"
        echo "task_metrics_calculator_present=$TASK_METRICS_CALCULATOR_PRESENT"
        echo "task_metrics_calculator_merged=$TASK_METRICS_CALCULATOR_MERGED"
        echo "task_anomaly_detection_present=$TASK_ANOMALY_DETECTION_PRESENT"
        echo "task_anomaly_detection_merged=$TASK_ANOMALY_DETECTION_MERGED"
        echo "task_report_generation_present=$TASK_REPORT_GENERATION_PRESENT"
        echo "task_report_generation_merged=$TASK_REPORT_GENERATION_MERGED"
        echo "task_cli_interface_present=$TASK_CLI_INTERFACE_PRESENT"
        echo "task_cli_interface_merged=$TASK_CLI_INTERFACE_MERGED"
        echo "present_required_branches=$PRESENT_REQUIRED_JOINED"
        echo "merged_required_branches=$MERGED_REQUIRED_JOINED"
        echo "missing_required_branches=$MISSING_REQUIRED_JOINED"
        echo "last_five_messages<<EOF"
        printf '%s\n' "$LAST_FIVE_MESSAGES"
        echo "EOF"
    } >> "$GITHUB_OUTPUT"
fi

echo "=== GIT WORKFLOW REPORT ==="
echo "   Current branch:              $CURRENT_BRANCH"
echo "   History reference:           $HISTORY_REF"
echo "   Commits (non-merge):         $COMMIT_COUNT"
echo "   Conventional-format commits: $CONVENTIONAL_COUNT / $COMMIT_COUNT"
echo "   Vague commit messages:       $BAD_MESSAGE_COUNT"
echo "   Feature branches found:      $FEATURE_BRANCH_COUNT"
echo "   Required branches present:   $REQUIRED_BRANCH_COUNT / ${#EXPECTED_BRANCHES[@]}"
echo "   Required branches merged:    $MERGED_REQUIRED_COUNT / ${#EXPECTED_BRANCHES[@]}"
echo "   branch_history.txt present:  $BRANCH_HISTORY_PRESENT"
echo "   10+ commits requirement met: $COMMIT_COUNT_MET ($COMMIT_COUNT / $COMMIT_COUNT_TARGET)"
echo "   Commit quality requirement:  $COMMIT_QUALITY_MET"
echo ""
echo "Task checklist:"
echo "- Part 1 config-loader branch created:       $TASK_CONFIG_LOADER_PRESENT"
echo "- Part 1 config-loader merged:               $TASK_CONFIG_LOADER_MERGED"
echo "- Part 2 pipeline-parser branch created:     $TASK_PIPELINE_PARSER_PRESENT"
echo "- Part 2 pipeline-parser merged:             $TASK_PIPELINE_PARSER_MERGED"
echo "- Part 3 metrics-calculator branch created:  $TASK_METRICS_CALCULATOR_PRESENT"
echo "- Part 3 metrics-calculator merged:          $TASK_METRICS_CALCULATOR_MERGED"
echo "- Part 4 anomaly-detection branch created:   $TASK_ANOMALY_DETECTION_PRESENT"
echo "- Part 4 anomaly-detection merged:           $TASK_ANOMALY_DETECTION_MERGED"
echo "- Part 5 report-generation branch created:   $TASK_REPORT_GENERATION_PRESENT"
echo "- Part 5 report-generation merged:           $TASK_REPORT_GENERATION_MERGED"
echo "- Part 6 cli-interface branch created:       $TASK_CLI_INTERFACE_PRESENT"
echo "- Part 6 cli-interface merged:               $TASK_CLI_INTERFACE_MERGED"
echo ""
echo "Workflow requirements:"
echo "- 10+ commits met:       $COMMIT_COUNT_MET ($COMMIT_COUNT / $COMMIT_COUNT_TARGET)"
echo "- branch_history.txt:    $BRANCH_HISTORY_PRESENT"
echo "- commit quality met:    $COMMIT_QUALITY_MET"
echo "- vague commit messages: $BAD_MESSAGE_COUNT"
echo ""
echo "Missing required branches:"
echo "- $MISSING_REQUIRED_JOINED"
echo ""
echo "Recent commits:"
if [ -n "$LAST_FIVE_MESSAGES" ]; then
    printf '%s\n' "$LAST_FIVE_MESSAGES"
else
    echo "- No commits found"
fi
echo ""
echo "⚠️  Git workflow remains a manual grading category."
echo "   This report checks expected feature branches, merge status, branch_history.txt,"
echo "   commit count, and basic commit-message quality,"
echo "   but the instructor still determines the final score."

exit 0
